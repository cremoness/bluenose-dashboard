"""
apply_changes.py
────────────────
Aplica el archivo changes_YYYY-MM-DD.json (exportado desde el dashboard)
a TASKS.md y regenera data.js automáticamente.

Uso:
    python apply_changes.py                         # usa el changes más reciente
    python apply_changes.py changes_2026-03-23.json
"""

import json
import os
import re
import sys
import glob
from datetime import datetime

TASKS_FILE = "TASKS.md"


def find_changes_file():
    files = sorted(glob.glob("changes_*.json"), reverse=True)
    if not files:
        print("No se encontro ningun archivo changes_*.json en esta carpeta.")
        sys.exit(1)
    return files[0]


def normalize(text):
    return re.sub(r'\s+', ' ', text.strip().lower())


def apply_to_tasks_md(changes):
    with open(TASKS_FILE, encoding="utf-8") as f:
        lines = f.readlines()

    done_texts     = {normalize(t["text"]) for t in changes.get("done", [])}
    approved_texts = {normalize(t["text"]) for t in changes.get("approved", [])}
    edited_map     = {normalize(t["original"]): t["edited"] for t in changes.get("edited", [])}
    rejected_texts = {normalize(t["text"]) for t in changes.get("rejected", [])}

    done_count = edited_count = 0
    new_lines = []

    for line in lines:
        m = re.match(r'^(\s*- \[)([ x])(\] .+)', line)
        if not m:
            new_lines.append(line)
            continue

        prefix, state, rest = m.group(1), m.group(2), m.group(3)
        plain = re.sub(r'\*\*\[.*?\]\*\*\s*', '', rest[2:])
        plain = re.sub(r'\| Owner:.*', '', plain)
        key = normalize(plain)

        if key in edited_map:
            rest = '] ' + edited_map[key]
            edited_count += 1

        if state == ' ' and (key in done_texts or key in approved_texts):
            state = 'x'
            done_count += 1

        if key in rejected_texts and state == ' ':
            continue

        new_lines.append(f"{prefix}{state}{rest}")

    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return done_count, edited_count


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else find_changes_file()
    print(f"Aplicando: {path}")

    if not os.path.exists(path):
        print(f"Archivo no encontrado: {path}")
        sys.exit(1)

    with open(path, encoding="utf-8") as f:
        changes = json.load(f)

    print(f"  Exportado: {changes.get('exported_at', '?')}")
    print(f"  Done: {len(changes.get('done',[]))} | Edited: {len(changes.get('edited',[]))} | "
          f"Approved: {len(changes.get('approved',[]))} | Rejected: {len(changes.get('rejected',[]))}")

    done_count, edited_count = apply_to_tasks_md(changes)
    print(f"\nTASKS.md actualizado — {done_count} completadas, {edited_count} editadas")

    if os.path.exists("build_data.py"):
        print("Regenerando data.js...")
        os.system("python build_data.py")
        print("data.js regenerado")
    else:
        print("build_data.py no encontrado — regenera data.js manualmente")

    backup = path.replace(".json", f"_applied_{datetime.now().strftime('%H%M')}.json")
    os.rename(path, backup)
    print(f"Backup guardado: {backup}")


if __name__ == "__main__":
    main()
