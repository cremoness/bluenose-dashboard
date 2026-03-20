#!/usr/bin/env python3
"""
fireflies_sync.py — Sincronización automática Fireflies.ai → TASKS.md
Blue Nose Dashboard | Ángelito Chanamé

Flujo:
  1. Se activa por GitHub Actions (webhook de Fireflies o schedule cada 30 min)
  2. Obtiene transcripciones nuevas desde la API de Fireflies
  3. Usa Claude AI para extraer tareas, acuerdos y pendientes
  4. Actualiza TASKS.md con los ítems en el formato correcto
  5. Hace commit y push automáticamente al repositorio

Variables de entorno requeridas (GitHub Actions Secrets):
  FIREFLIES_API_KEY   — API key de Fireflies.ai (plan Business)
  ANTHROPIC_API_KEY   — API key de Anthropic para Claude
  GH_TOKEN            — GitHub token con permisos de escritura al repo (para commit)
  TRANSCRIPT_ID       — (opcional) ID específico de transcripción a procesar
"""

import os
import re
import json
import datetime
import subprocess
import urllib.request
import urllib.parse
import urllib.error

# ── Configuración ────────────────────────────────────────────────────────────
FIREFLIES_API_KEY  = os.environ.get("FIREFLIES_API_KEY", "")
ANTHROPIC_API_KEY  = os.environ.get("ANTHROPIC_API_KEY", "")
TRANSCRIPT_ID      = os.environ.get("TRANSCRIPT_ID", "")          # opcional
LAST_SYNC_FILE     = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".fireflies_last_sync")
TASKS_PATH         = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TASKS.md")

MESES_ES = {
    1:"enero",2:"febrero",3:"marzo",4:"abril",5:"mayo",6:"junio",
    7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"
}

CLIENT_MAP = {
    "ucsp": "UCSP", "world vision": "WV", "wv": "WV",
    "upsjb": "UPSJB", "virtualpos": "VP CHILE", "virtual pos": "VP CHILE",
    "chile": "VP CHILE", "smartimper": "Smartimper", "caja ica": "Caja Ica",
    "cendes": "CENDES", "simma": "SIMMA",
}

# ── Fireflies API ────────────────────────────────────────────────────────────

def fireflies_request(query: str, variables: dict = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.fireflies.ai/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {FIREFLIES_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def get_transcript(transcript_id: str) -> dict:
    """Obtiene una transcripción completa por ID."""
    query = """
    query GetTranscript($id: String!) {
      transcript(id: $id) {
        id
        title
        date
        duration
        organizer_email
        participants
        summary {
          keywords
          action_items
          overview
          outline
          shorthand_bullet
        }
        sentences {
          speaker_name
          text
          start_time
        }
      }
    }
    """
    result = fireflies_request(query, {"id": transcript_id})
    return result.get("data", {}).get("transcript", {})


def get_recent_transcripts(since_timestamp: int = None, limit: int = 10) -> list:
    """Obtiene transcripciones recientes, opcionalmente filtradas por fecha."""
    query = """
    query {
      transcripts(limit: %d) {
        id
        title
        date
        duration
        organizer_email
        participants
        summary {
          action_items
          overview
          shorthand_bullet
        }
      }
    }
    """ % limit
    result = fireflies_request(query)
    transcripts = result.get("data", {}).get("transcripts", [])

    if since_timestamp:
        transcripts = [
            t for t in transcripts
            if t.get("date") and int(t["date"]) / 1000 > since_timestamp
        ]
    return transcripts


def get_last_sync_timestamp() -> int:
    """Lee el timestamp de la última sincronización."""
    if os.path.exists(LAST_SYNC_FILE):
        with open(LAST_SYNC_FILE, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                return int(content)
    # Si no existe, devuelve hace 2 horas
    return int(datetime.datetime.utcnow().timestamp()) - 7200


def save_last_sync_timestamp():
    """Guarda el timestamp actual como última sincronización."""
    with open(LAST_SYNC_FILE, "w") as f:
        f.write(str(int(datetime.datetime.utcnow().timestamp())))


# ── Claude AI — Extracción de tareas ────────────────────────────────────────

def extract_tasks_with_claude(transcript: dict) -> dict:
    """
    Usa Claude para analizar la transcripción y extraer tareas estructuradas
    en el formato exacto de TASKS.md de Blue Nose.
    """
    title       = transcript.get("title", "Reunión sin título")
    date_epoch  = transcript.get("date", 0)
    participants = transcript.get("participants", [])
    summary     = transcript.get("summary", {})
    sentences   = transcript.get("sentences", [])

    # Fecha legible
    try:
        dt = datetime.datetime.fromtimestamp(int(date_epoch) / 1000)
        date_str = f"{dt.day:02d}.{dt.month:02d}"
    except Exception:
        date_str = datetime.date.today().strftime("%d.%m")

    # Construir texto de la reunión para Claude
    overview = summary.get("overview", "")
    action_items = summary.get("action_items", "")
    shorthand = summary.get("shorthand_bullet", "")

    transcript_text = "\n".join([
        s.get("text", "") for s in sentences[:200]  # primeras 200 frases
    ]) if sentences else ""

    meeting_content = f"""
TÍTULO: {title}
FECHA: {date_str}
PARTICIPANTES: {', '.join(participants)}

RESUMEN:
{overview}

ACTION ITEMS DE FIREFLIES:
{action_items}

PUNTOS CLAVE:
{shorthand}

FRAGMENTO DE TRANSCRIPCIÓN:
{transcript_text[:3000]}
""".strip()

    prompt = f"""Eres el asistente de Ángelito Chanamé de Blue Nose, una consultora de HubSpot y marketing digital.

Analiza esta reunión y extrae TODAS las tareas, acuerdos, pendientes y follow-ups mencionados.

CLIENTES ACTIVOS DE BLUE NOSE:
- UCSP (universidad, Agente IA, Mesa de Ayuda, Coaching)
- World Vision / WV (Perú, Honduras, España, Chile, Ecuador, Rep. Dominicana)
- UPSJB (educación a distancia)
- VirtualPos / VP CHILE (HubSpot, donaciones)
- Smartimper (BDR)
- Caja Ica

MIEMBROS DEL EQUIPO:
Ángelito, Enrique, Pablo, Cristian P, Sofía, Marcos, Valeria, Carlos, Estuardo, Luis, Diana, Ornella

---

REUNIÓN A ANALIZAR:
{meeting_content}

---

Responde ÚNICAMENTE con un JSON válido con esta estructura exacta:

{{
  "client": "nombre del cliente principal detectado (ej: UCSP, WV HND, UPSJB, VP CHILE, etc.)",
  "meeting_title": "título corto descriptivo de la reunión",
  "urgent": [
    {{
      "text": "descripción clara y accionable de la tarea urgente",
      "owner": "nombre del responsable (si se menciona, si no: 'Ángelito')"
    }}
  ],
  "weekly": [
    {{
      "text": "descripción clara y accionable de la tarea de esta semana",
      "owner": "nombre del responsable"
    }}
  ],
  "agreements": [
    "acuerdo o decisión tomada en la reunión (formato informativo)"
  ],
  "completed": [
    "tarea que se confirmó como completada durante la reunión"
  ]
}}

REGLAS:
- Sé específico y accionable en cada tarea
- Captura TODOS los compromisos, no solo los obvios
- Si el responsable no está claro, asigna a Ángelito
- Las tareas urgentes son para HOY o MAÑANA; las weekly son para esta semana
- Si algo quedó pendiente de reuniones anteriores y se volvió a mencionar, inclúyelo
- Máximo 8 items por categoría
- Si no hay items para una categoría, deja el array vacío []
"""

    payload = json.dumps({
        "model": "claude-3-5-haiku-20241022",
        "max_tokens": 2000,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            response = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        raise RuntimeError(f"Anthropic API error {e.code}: {error_body}")

    content = response["content"][0]["text"].strip()

    # Extraer JSON de la respuesta
    json_match = re.search(r'\{.*\}', content, re.DOTALL)
    if json_match:
        return json.loads(json_match.group()), date_str
    raise ValueError(f"Claude no devolvió JSON válido:\n{content}")


# ── Actualización de TASKS.md ────────────────────────────────────────────────

def detect_client_tag(text: str, default: str = "") -> str:
    """Detecta el cliente en base al texto."""
    text_lower = text.lower()
    for key, val in CLIENT_MAP.items():
        if key in text_lower:
            return val
    return default


def format_task_line(text: str, owner: str, client_tag: str, date_str: str) -> str:
    """Formatea una tarea en el estilo de TASKS.md."""
    tag = f"[{client_tag} 🆕 {date_str}]" if client_tag else f"[🆕 {date_str}]"
    return f"- [ ] **{tag}** {text} | Owner: {owner}"


def update_tasks_md(extracted: dict, date_str: str, transcript_title: str):
    """Inserta las tareas extraídas en las secciones correctas de TASKS.md."""
    if not os.path.exists(TASKS_PATH):
        print(f"[ERROR] No se encontró TASKS.md en: {TASKS_PATH}")
        return False

    with open(TASKS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    client    = extracted.get("client", "")
    urgent    = extracted.get("urgent", [])
    weekly    = extracted.get("weekly", [])
    completed = extracted.get("completed", [])

    today = datetime.date.today()
    today_str = f"{today.year}-{today.month:02d}-{today.day:02d}"

    # ── Actualizar cabecera con fecha y reunión ──
    header_line = content.split("\n")[1] if "\n" in content else ""
    new_source = f"Reunión Fireflies: {transcript_title} {date_str}"
    if header_line.startswith(">"):
        if new_source not in header_line:
            new_header = re.sub(
                r"(> Última actualización:.*)",
                f"> Última actualización: {today_str} | {new_source}",
                content,
                count=1
            )
            content = new_header

    # ── Insertar tareas URGENTES ──
    if urgent:
        urgente_lines = []
        for item in urgent:
            line = format_task_line(
                item["text"], item["owner"],
                client, date_str
            )
            urgente_lines.append(line)

        insert_block = "\n".join(urgente_lines)
        # Insertar después de la línea "## 🔴 URGENTE / Hoy mismo"
        content = re.sub(
            r"(## 🔴 URGENTE / Hoy mismo\n)",
            f"\\1\n{insert_block}\n",
            content
        )
        print(f"  ✅ {len(urgente_lines)} tarea(s) urgente(s) insertadas")

    # ── Insertar tareas SEMANALES ──
    if weekly:
        weekly_lines = []
        for item in weekly:
            line = format_task_line(
                item["text"], item["owner"],
                client, date_str
            )
            weekly_lines.append(line)

        insert_block = "\n".join(weekly_lines)

        # Buscar subsección del cliente dentro de 🟡
        client_section_pattern = rf"(### {re.escape(client)}[^\n]*\n)"
        if re.search(client_section_pattern, content):
            content = re.sub(
                client_section_pattern,
                f"\\1{insert_block}\n",
                content,
                count=1
            )
        else:
            # Si no existe sección del cliente, insertar al inicio de 🟡
            content = re.sub(
                r"(## 🟡 PRÓXIMAS / Esta semana\n)",
                f"\\1\n### {client} ⚠️ ACTUALIZADO {date_str}\n{insert_block}\n",
                content
            )
        print(f"  ✅ {len(weekly_lines)} tarea(s) semanal(es) insertadas bajo [{client}]")

    # ── Insertar COMPLETADAS ──
    if completed:
        completed_lines = []
        for item in completed:
            completed_lines.append(f"- [x] **[{client} ✅ {date_str}]** {item}")

        insert_block = "\n".join(completed_lines)
        content = re.sub(
            r"(## ✅ COMPLETADO\n)",
            f"\\1\n{insert_block}\n",
            content
        )
        print(f"  ✅ {len(completed_lines)} tarea(s) completada(s) marcadas")

    with open(TASKS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    return True


# ── Git commit y push ────────────────────────────────────────────────────────

def git_commit_and_push(transcript_title: str, date_str: str):
    """Hace commit de TASKS.md y .fireflies_last_sync al repositorio."""
    try:
        subprocess.run(["git", "config", "user.email", "bot@bluenose.ai"], check=True)
        subprocess.run(["git", "config", "user.name", "BlueNose Bot"], check=True)
        subprocess.run(["git", "add", "TASKS.md", ".fireflies_last_sync"], check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"])
        if result.returncode == 0:
            print("  ℹ️  Sin cambios para commitear")
            return
        commit_msg = f"sync: Fireflies → TASKS.md | {transcript_title} [{date_str}]"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push"], check=True)
        print("  ✅ Commit y push realizados")
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Error en git: {e}")


# ── Main ─────────────────────────────────────────────────────────────────────

def process_transcript(transcript_id: str):
    """Procesa una transcripción específica."""
    print(f"\n📥 Obteniendo transcripción {transcript_id}...")
    transcript = get_transcript(transcript_id)
    if not transcript:
        print(f"  ❌ No se encontró la transcripción {transcript_id}")
        return

    title = transcript.get("title", "Sin título")
    print(f"  📋 Reunión: {title}")
    print(f"  👥 Participantes: {', '.join(transcript.get('participants', []))}")

    print("\n🤖 Analizando con Claude AI...")
    extracted, date_str = extract_tasks_with_claude(transcript)

    client = extracted.get("client", "?")
    print(f"  🏷️  Cliente detectado: {client}")
    print(f"  🔴 Urgentes: {len(extracted.get('urgent', []))}")
    print(f"  🟡 Semanales: {len(extracted.get('weekly', []))}")
    print(f"  ✅ Completadas: {len(extracted.get('completed', []))}")
    print(f"  🤝 Acuerdos: {len(extracted.get('agreements', []))}")

    print("\n📝 Actualizando TASKS.md...")
    updated = update_tasks_md(extracted, date_str, title)

    if updated:
        save_last_sync_timestamp()
        print("\n🔄 Haciendo commit al repositorio...")
        git_commit_and_push(title, date_str)
        print(f"\n✅ Sincronización completa: [{title}] → TASKS.md")
    else:
        print("\n❌ No se pudo actualizar TASKS.md")


def main():
    if not FIREFLIES_API_KEY:
        print("❌ FIREFLIES_API_KEY no configurada. Agrega el Secret en GitHub Actions.")
        return
    if not ANTHROPIC_API_KEY:
        print("❌ ANTHROPIC_API_KEY no configurada. Agrega el Secret en GitHub Actions.")
        return

    # Modo 1: transcript específico (pasado por webhook o manualmente)
    if TRANSCRIPT_ID:
        print(f"🎯 Modo: transcript específico → {TRANSCRIPT_ID}")
        process_transcript(TRANSCRIPT_ID)
        return

    # Modo 2: buscar transcripciones nuevas desde última sync
    last_sync = get_last_sync_timestamp()
    last_sync_dt = datetime.datetime.fromtimestamp(last_sync).strftime("%d/%m/%Y %H:%M")
    print(f"🔍 Modo: búsqueda de reuniones nuevas desde {last_sync_dt}")

    transcripts = get_recent_transcripts(since_timestamp=last_sync, limit=10)

    if not transcripts:
        print("  ℹ️  No hay transcripciones nuevas desde la última sincronización.")
        return

    print(f"  📋 {len(transcripts)} transcripción(es) nueva(s) encontrada(s)")
    for t in transcripts:
        process_transcript(t["id"])


if __name__ == "__main__":
    main()
