#!/usr/bin/env python3
"""
fireflies_sync.py — Sincronización automática Fireflies.ai → TASKS.md
Blue Nose Dashboard | Ángelito Chanamé
VERSION: 2.0 — usa summaries de Fireflies directamente (sin Claude API)

Variables de entorno requeridas (GitHub Actions Secrets):
  FIREFLIES_API_KEY  — API key de Fireflies.ai (plan Business)
  TRANSCRIPT_ID      — (opcional) ID específico de transcripción
"""

import os, re, json, datetime, subprocess, sys, io
import urllib.request, urllib.parse, urllib.error

# Forzar salida en UTF-8 para evitar UnicodeEncodeError con emojis en Windows
if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FIREFLIES_API_KEY = os.environ.get("FIREFLIES_API_KEY", "")
TRANSCRIPT_ID     = os.environ.get("TRANSCRIPT_ID", "")
BASE_DIR          = os.path.dirname(os.path.abspath(__file__))
LAST_SYNC_FILE    = os.path.join(BASE_DIR, ".fireflies_last_sync")
TASKS_PATH        = os.path.join(BASE_DIR, "TASKS.md")

print("## VERSION 2.0 — Fireflies summaries directo ##")

CLIENT_MAP = {
    "ucsp": "UCSP", "world vision": "WV", "wv ": "WV",
    "upsjb": "UPSJB", "virtualpos": "VP CHILE", "virtual pos": "VP CHILE",
    " chile": "VP CHILE", "smartimper": "Smartimper", "caja ica": "Caja Ica",
    "cendes": "CENDES", "simma": "SIMMA",
}

# ── Fireflies API ─────────────────────────────────────────────────────────────

def fireflies_gql(query: str, variables: dict = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        "https://api.fireflies.ai/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {FIREFLIES_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Fireflies API error {e.code}: {e.read().decode()}")


def get_transcript(tid: str) -> dict:
    q = """
    query GetTranscript($id: String!) {
      transcript(id: $id) {
        id title date duration organizer_email participants
        summary { keywords action_items overview shorthand_bullet }
      }
    }"""
    return fireflies_gql(q, {"id": tid}).get("data", {}).get("transcript", {})


def get_recent_transcripts(since_ts: int, limit: int = 10) -> list:
    q = """query { transcripts(limit: %d) {
      id title date participants
      summary { action_items overview }
    } }""" % limit
    all_t = fireflies_gql(q).get("data", {}).get("transcripts", [])
    return [t for t in all_t if t.get("date") and int(t["date"]) / 1000 > since_ts]


def last_sync_ts() -> int:
    if os.path.exists(LAST_SYNC_FILE):
        c = open(LAST_SYNC_FILE).read().strip()
        if c.isdigit():
            return int(c)
    return int(datetime.datetime.now(datetime.timezone.utc).timestamp()) - 7200


def save_sync_ts():
    open(LAST_SYNC_FILE, "w").write(str(int(datetime.datetime.now(datetime.timezone.utc).timestamp())))


# ── Parsear summary de Fireflies → tareas ────────────────────────────────────

def detect_client(text: str) -> str:
    tl = text.lower()
    for key, val in CLIENT_MAP.items():
        if key in tl:
            return val
    return "General"


def detect_owner(line: str) -> str:
    owners = ["ángelito","angelito","enrique","pablo","cristian","sofía","sofia",
              "marcos","valeria","carlos","estuardo","luis","diana","ornella"]
    ll = line.lower()
    for o in owners:
        if o in ll:
            return o.capitalize()
    return "Ángelito"


def parse_action_items(text: str) -> list:
    """Convierte el texto de action_items de Fireflies en lista de dicts."""
    items = []
    if not text:
        return items
    for line in text.replace("\r", "").split("\n"):
        line = line.strip().lstrip("-•*·123456789.").strip()
        if len(line) < 10:
            continue
        items.append({"text": line[:200], "owner": detect_owner(line)})
    return items[:8]


def format_task(text: str, owner: str, client: str, date_str: str) -> str:
    tag = f"[{client} 🆕 {date_str}]" if client and client != "General" else f"[🆕 {date_str}]"
    return f"- [ ] **{tag}** {text} | Owner: {owner}"


# ── Actualizar TASKS.md ───────────────────────────────────────────────────────

def update_tasks(transcript: dict):
    title    = transcript.get("title", "Reunión sin título")
    summary  = transcript.get("summary") or {}
    ai_text  = summary.get("action_items", "") or ""
    overview = (summary.get("overview", "") or "").strip()
    parts    = transcript.get("participants", []) or []

    try:
        dt = datetime.datetime.fromtimestamp(int(transcript.get("date", 0)) / 1000)
        date_str = f"{dt.day:02d}.{dt.month:02d}"
    except Exception:
        date_str = datetime.date.today().strftime("%d.%m")

    context = f"{title} {ai_text} {overview} {' '.join(parts)}"
    client  = detect_client(context)
    items   = parse_action_items(ai_text)

    if not items and overview:
        # Si no hay action_items, usar el overview como una tarea de seguimiento
        items = [{"text": f"Revisar acuerdos de reunión: {overview[:150]}", "owner": "Ángelito"}]

    print(f"\n  🏷️  Cliente: {client}")
    print(f"  📋 Título: {title}")
    print(f"  ✅ Action items detectados: {len(items)}")
    for it in items:
        print(f"     · [{it['owner']}] {it['text'][:80]}")

    if not items:
        print("  ℹ️  Sin tareas para agregar.")
        return False

    with open(TASKS_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    today_str = datetime.date.today().strftime("%Y-%m-%d")

    # Actualizar cabecera
    content = re.sub(
        r"(> Última actualización:)[^\n]*",
        f"\\1 {today_str} | Reunión Fireflies: {title} {date_str}",
        content, count=1
    )

    # Construir bloque de tareas
    task_lines = "\n".join(format_task(i["text"], i["owner"], client, date_str) for i in items)

    # Insertar en sección del cliente dentro de 🟡, o al inicio de 🟡
    client_pat = rf"(### {re.escape(client)}[^\n]*\n)"
    if re.search(client_pat, content):
        content = re.sub(client_pat, f"\\1{task_lines}\n", content, count=1)
    else:
        content = re.sub(
            r"(## 🟡 PRÓXIMAS / Esta semana\n)",
            f"\\1\n### {client} ⚠️ ACTUALIZADO {date_str}\n{task_lines}\n",
            content
        )

    with open(TASKS_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ TASKS.md actualizado con {len(items)} tarea(s)")
    return True


# ── Git commit/push ───────────────────────────────────────────────────────────

def git_push(title: str, date_str: str):
    try:
        subprocess.run(["git","config","user.email","bot@bluenose.ai"], check=True)
        subprocess.run(["git","config","user.name","BlueNose Bot"], check=True)
        subprocess.run(["git","add","TASKS.md",".fireflies_last_sync"], check=True)
        diff = subprocess.run(["git","diff","--cached","--quiet"])
        if diff.returncode == 0:
            print("  ℹ️  Sin cambios nuevos para commitear.")
            return
        subprocess.run(["git","commit","-m",f"sync: Fireflies → TASKS.md | {title} [{date_str}]"], check=True)
        subprocess.run(["git","push"], check=True)
        print("  ✅ Commit y push realizados.")
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Git error: {e}")


# ── Main ──────────────────────────────────────────────────────────────────────

def process(tid: str):
    print(f"\n📥 Obteniendo transcripción {tid}...")
    t = get_transcript(tid)
    if not t:
        print(f"  ❌ Transcripción no encontrada: {tid}")
        return
    try:
        dt = datetime.datetime.fromtimestamp(int(t.get("date", 0)) / 1000)
        date_str = f"{dt.day:02d}.{dt.month:02d}"
    except Exception:
        date_str = datetime.date.today().strftime("%d.%m")
    updated = update_tasks(t)
    if updated:
        save_sync_ts()
        git_push(t.get("title", "reunión"), date_str)


def main():
    if not FIREFLIES_API_KEY:
        print("❌ FIREFLIES_API_KEY no configurada.")
        return

    if TRANSCRIPT_ID:
        print(f"🎯 Modo: transcript específico → {TRANSCRIPT_ID}")
        process(TRANSCRIPT_ID)
        return

    since = last_sync_ts()
    dt_str = datetime.datetime.fromtimestamp(since).strftime("%d/%m/%Y %H:%M")
    print(f"🔍 Buscando reuniones nuevas desde {dt_str}...")
    transcripts = get_recent_transcripts(since_ts=since)
    if not transcripts:
        print("  ℹ️  Sin reuniones nuevas.")
        return
    print(f"  📋 {len(transcripts)} reunión(es) encontrada(s)")
    for t in transcripts:
        process(t["id"])


if __name__ == "__main__":
    main()
