import os
import re
import json

def get_account_from_header(header):
    h = header.lower()
    if "bluenose" in h or "bn" in h: return "BLUENOSE"
    if "ucsp" in h or "cendes" in h: return "UCSP"
    if "wv" in h or "world vision" in h or "simma" in h: return "WV"
    if "upsjb" in h: return "UPSJB"
    if "vp" in h or "virtualpos" in h or "chile" in h: return "VP"
    if "smartimper" in h: return "Smartimper"
    if "ica" in h: return "Ica"
    return "General"

def parse_tag(raw_tag, current_account):
    tag_clean = raw_tag.replace("🆕", "").strip()
    tag_clean = re.sub(r'\d{1,2}\.\d{1,2}(?:\.\d{2})?', '', tag_clean).strip()
    
    if not tag_clean:
        return current_account, "General"
        
    parts = [p.strip() for p in tag_clean.split('—')]
    account = current_account
    project = "General"
    
    if len(parts) > 1:
        acct_str = parts.pop(0)
        project = " — ".join(parts)
        account = get_account_from_header(acct_str)
        if account == "General": account = current_account # fallback
    else:
        val = parts[0]
        v = val.lower()
        acct_candidate = get_account_from_header(v)
        if acct_candidate != "General":
            account = acct_candidate
            project = "General"
        else:
            if v.startswith("wv "): 
                account = "WV"
                project = val.split(" ", 1)[1].strip()
            elif v.startswith("vp "):
                account = "VP"
                project = val.split(" ", 1)[1].strip()
            else:
                project = val

    return account if account else "General", project

def get_tag_class(account):
    m = {
        "UCSP": "tag-uc",
        "WV": "tag-wv",
        "UPSJB": "tag-up",
        "VP": "tag-vp",
        "Smartimper": "tag-sm",
        "Ica": "tag-ci",
        "BLUENOSE": "tag-bn"
    }
    return m.get(account, "tag-def")

def parse_tasks(path):
    tasks = {"urgente": [], "semana": [], "mes": [], "done": []}
    
    if not os.path.exists(path):
        return tasks
        
    current_section = ""
    current_account = "General"
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "🔴" in line:
                current_section = "urgente"
                current_account = "General"
            elif "🟡" in line:
                current_section = "semana"
                current_account = "General"
            elif "🟢" in line:
                current_section = "mes"
                current_account = "General"
            elif line.startswith("### "):
                current_account = get_account_from_header(line.replace("### ", ""))
            elif line.startswith("## ") and "COMPLETADO" in line:
                current_section = "done"
                current_account = "General"
                
            if current_section and re.match(r"^\s*- \[( |x|X|✅)\]", line):
                is_new = "🆕" in line or "NUEVO" in line
                is_completed = bool(re.search(r"^\s*- \[(x|X|✅)\]", line)) or current_section == "done"
                
                clean = re.sub(r"^\s*- \[( |x|X|✅)\]\s*", "", line)
                
                owner = ""
                if "| Owner:" in clean:
                    parts = clean.split("| Owner:")
                    clean = parts[0].strip()
                    owner = parts[1].strip()
                elif "Owner:" in clean:
                    parts = clean.split("Owner:")
                    clean = parts[0].replace("|", "").strip()
                    owner = parts[1].strip()
                
                raw_tag = ""
                m = re.search(r'\*\*\[(.*?)\]\*\*', clean)
                if m:
                    raw_tag = m.group(1)
                    clean = re.sub(r"^\*\*\[.*?\]\*\*\s*", "", clean)
                    
                account, project = parse_tag(raw_tag, current_account)
                
                due = ""
                if "Due:" in owner:
                    oparts = owner.split("Due:")
                    owner = oparts[0].replace("|", "").strip()
                    due = oparts[1].strip()
                
                clean = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", clean)
                clean = re.sub(r"\s*·\s*$", "", clean)
                
                task_obj = {
                    "text": clean,
                    "account": account,
                    "project": project,
                    "tag": account if project == "General" else project,
                    "tagClass": get_tag_class(account),
                    "owner": owner.strip("· ").strip(),
                    "clients": [account] if account != "General" else [],
                }
                if is_new: task_obj["isNew"] = True
                if is_completed: task_obj["isCompleted"] = True
                if due: task_obj["due"] = due
                    
                tasks[current_section].append(task_obj)
                
    return tasks

if __name__ == "__main__":
    tasks_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TASKS.md")
    data = parse_tasks(tasks_path)
    
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("const TASKS = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")
    print(f"Generated {output_path} successfully.")
