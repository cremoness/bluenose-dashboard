#!/usr/bin/env python3
"""
daily_brief.py — Resumen diario de Blue Nose para Ángelito Chanamé
Envía un mensaje a Telegram + Discord con pendientes, reuniones y prioridades del día.
Para correr en PythonAnywhere con cron task a las 8:20am (America/Lima).
"""

import json
import urllib.request
import urllib.parse
import datetime
import re
import os
import sys

# ── Configuración ──────────────────────────────────────────────────────────────
# Lee credenciales desde variables de entorno (GitHub Actions Secrets)
# o usa los valores directos como fallback local
import os

TELEGRAM_TOKEN   = os.environ.get('TELEGRAM_TOKEN', '')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')
DISCORD_WEBHOOK  = os.environ.get('DISCORD_WEBHOOK', 'https://discord.com/api/webhooks/1483973136000221185/P64sL5fi9K0U9hEVbNnHLyqk74NH1U7k_EA3dGo6PjPeHFIfx2waNLmEC6TcVtFlG-m4')

# En GitHub Actions el archivo TASKS.md estará junto al script
TASKS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TASKS.md")
# ───────────────────────────────────────────────────────────────────────────────

DIAS_ES = {
    0: "Lunes", 1: "Martes", 2: "Miércoles",
    3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"
}
MESES_ES = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

CLIENT_EMOJI = {
    "UCSP": "🏛", "World Vision": "🌍", "WV": "🌍",
    "UPSJB": "🎓", "VirtualPos": "💳", "Smartimper": "⚡",
    "Caja Ica": "🏦", "CENDES": "🏛", "SIMMA": "🌍",
}

TELEGRAM_SPECIAL = ['_','*','[',']','(',')','>','#','+','-','=','|','{','}','.','!','~','`']

def esc(s):
    """Escapa caracteres especiales para MarkdownV2 de Telegram."""
    for c in TELEGRAM_SPECIAL:
        s = s.replace(c, "\\" + c)
    return s

def get_emoji(text):
    for client, emoji in CLIENT_EMOJI.items():
        if client.lower() in text.lower():
            return emoji
    return "•"

def parse_tasks(path):
    urgente, semana, followup = [], [], []
    if not os.path.exists(path):
        print(f"[WARN] No se encontró TASKS.md en: {path}")
        return urgente, semana, followup

    current = None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "🔴" in line:   current = "r"
            elif "🟡" in line: current = "y"
            elif "🟢" in line: current = "y"
            elif line.startswith("##"): current = None

            if re.match(r"^\s*- \[ \]", line):
                clean = re.sub(r"^\s*- \[ \]\s*", "", line)
                clean = re.sub(r"\*\*\[.*?\]\*\*\s*", "", clean)
                clean = re.sub(r"\*\*(.*?)\*\*", r"\1", clean)
                clean = re.sub(r"\|.*$", "", clean).strip()
                if len(clean) < 10: continue
                if len(clean) > 85: clean = clean[:82] + "..."
                e = get_emoji(clean)
                if current == "r":   urgente.append(f"{e} {clean}")
                elif current == "y": semana.append(f"{e} {clean}")

            if "follow-up" in line.lower() or "escribirle al cliente" in line.lower():
                m = re.search(r"~(\d+\.\d+)", line)
                if m: followup.append(m.group(1))

    return urgente, semana, followup

def get_meetings(weekday):
    meetings = []
    if weekday == 0: meetings.append("📋 Status interno Blue Nose — inicio de semana")
    if weekday == 3: meetings.append("📋 Status interno Blue Nose — cierre de semana")
    if weekday == 2: meetings.append("🌍 WV HND — revisión piezas y WF con Luis y Pablo")
    if weekday == 3: meetings.append("🌍 WV HND — reunión con Express Pago")
    return meetings

def build_telegram_msg(urgente, semana, followup, meetings, today):
    dia   = DIAS_ES[today.weekday()]
    fecha = f"{today.day} de {MESES_ES[today.month]} de {today.year}"
    lines = [
        "☀️ *Buenos días, Ángelito\\!*",
        f"_{esc(dia)}, {esc(fecha)}_",
        "",
    ]
    if meetings:
        lines.append("📅 *Reuniones hoy:*")
        for m in meetings: lines.append(f"  {esc(m)}")
        lines.append("")
    if urgente:
        lines.append("🔴 *Urgente / Top prioridad:*")
        for i, t in enumerate(urgente[:5], 1): lines.append(f"  {i}\\. {esc(t)}")
        if len(urgente) > 5: lines.append(f"  _\\.\\.\\.y {len(urgente)-5} más en TASKS\\.md_")
        lines.append("")
    if semana:
        lines.append("🟡 *Pendientes de la semana:*")
        for i, t in enumerate(semana[:5], 1): lines.append(f"  {i}\\. {esc(t)}")
        if len(semana) > 5: lines.append(f"  _\\.\\.\\.y {len(semana)-5} más en TASKS\\.md_")
        lines.append("")
    if followup:
        lines.append("🔄 *Follow\\-ups programados:*")
        for fu in followup[:2]: lines.append(f"  ⚡ Smartimper: próximo follow\\-up \\~{esc(fu)}")
        lines.append("")
    lines.append("💪 _¡Buen día\\!_")
    return "\n".join(lines)

def build_discord_msg(urgente, semana, followup, meetings, today):
    dia   = DIAS_ES[today.weekday()]
    fecha = f"{today.day} de {MESES_ES[today.month]} de {today.year}"
    lines = [
        "☀️ **Buenos días, Ángelito!**",
        f"*{dia}, {fecha}*",
        "",
    ]
    if meetings:
        lines.append("📅 **Reuniones hoy:**")
        for m in meetings: lines.append(f"> {m}")
        lines.append("")
    if urgente:
        lines.append("🔴 **Urgente / Top prioridad:**")
        for i, t in enumerate(urgente[:5], 1): lines.append(f"> {i}. {t}")
        if len(urgente) > 5: lines.append(f"> *...y {len(urgente)-5} más en TASKS.md*")
        lines.append("")
    if semana:
        lines.append("🟡 **Pendientes de la semana:**")
        for i, t in enumerate(semana[:5], 1): lines.append(f"> {i}. {t}")
        if len(semana) > 5: lines.append(f"> *...y {len(semana)-5} más en TASKS.md*")
        lines.append("")
    if followup:
        lines.append("🔄 **Follow-ups programados:**")
        for fu in followup[:2]: lines.append(f"> ⚡ Smartimper: próximo follow-up ~{fu}")
        lines.append("")
    lines.append("💪 *¡Buen día!*")
    return "\n".join(lines)

def send_telegram(msg):
    url  = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "MarkdownV2"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())

def send_discord(msg):
    if not DISCORD_WEBHOOK:
        raise ValueError("DISCORD_WEBHOOK está vacío — verifica el Secret en GitHub Actions")
    payload = json.dumps({"content": msg, "username": "Blue Nose Daily"}).encode("utf-8")
    req = urllib.request.Request(
        DISCORD_WEBHOOK, data=payload,
        headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.status

def main():
    today = datetime.date.today()
    if today.weekday() >= 5:
        print(f"[daily_brief] Fin de semana — no se envía.")
        return

    urgente, semana, followup = parse_tasks(TASKS_PATH)
    meetings = get_meetings(today.weekday())

    tg_msg = build_telegram_msg(urgente, semana, followup, meetings, today)
    dc_msg = build_discord_msg(urgente, semana, followup, meetings, today)

    print("─── Telegram ───────────────────────────────────────")
    print(tg_msg)
    print("─── Discord ────────────────────────────────────────")
    print(dc_msg)
    print("────────────────────────────────────────────────────")

    # Enviar Telegram
    try:
        result = send_telegram(tg_msg)
        if result.get("ok"):
            print("✅ Telegram: mensaje enviado")
        else:
            print(f"❌ Telegram error: {result.get('description')}")
    except Exception as ex:
        print(f"❌ Telegram excepción: {ex}")

    # Enviar Discord
    print(f"[DEBUG] DISCORD_WEBHOOK configurado: {'Sí' if DISCORD_WEBHOOK else 'NO — Secret vacío'}")
    try:
        status = send_discord(dc_msg)
        if status in (200, 204):
            print("✅ Discord: mensaje enviado")
        else:
            print(f"❌ Discord status inesperado: {status}")
    except urllib.error.HTTPError as ex:
        body = ex.read().decode()
        print(f"❌ Discord HTTP {ex.code}: {body}")
    except Exception as ex:
        print(f"❌ Discord excepción: {ex}")

if __name__ == "__main__":
    main()
