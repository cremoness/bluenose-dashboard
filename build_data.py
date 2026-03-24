import os
import re
import json

# ── BlueNose Team ──────────────────────────────────────────────────────────────
TEAM_BN = [
    {"id": "enrique",  "name": "Enrique",   "role": "Socio y estratega",              "color": "#818cf8"},
    {"id": "pablo",    "name": "Pablo",      "role": "Socio, líder tecnología",        "color": "#60a5fa"},
    {"id": "cristian", "name": "Cristian",   "role": "Backend y soporte técnico",      "color": "#34d399"},
    {"id": "marcos",   "name": "Marcos",     "role": "Especialista en CRMs",           "color": "#fb923c"},
    {"id": "angelm",   "name": "Angel M.",   "role": "Soporte técnico",                "color": "#fbbf24"},
    {"id": "angelito", "name": "Ángelito",   "role": "Project manager y creativo",     "color": "#c084fc"},
]

# ── Client Directory ───────────────────────────────────────────────────────────
CLIENT_DIR = [
    # Smartimper
    {"client":"Smartimper","name":"Valdric Tardós","email":"valdric@smartimper.mx","phone":"+52 55 3097 4266","role":"CEO","canal":"Discord"},
    # WV RD
    {"client":"WV RD","name":"Juan Benalcazar","email":"juan_benalcazar@wvi.org","phone":"+593 99 650 6506","role":"Coordinador Marketing Digital","canal":"Discord"},
    {"client":"WV RD","name":"Johmara Vargas","email":"johmara_vargas@wvi.org","phone":"+593 98 343 3403","role":"Gerente de Marketing (secondment)","canal":"Urgencias WP"},
    {"client":"WV RD","name":"Erick Urbaez","email":"erick_urbaez@wvi.org","phone":"","role":"Creador de Contenido y Community Manager","canal":"Discord"},
    {"client":"WV RD","name":"Argenis Perez","email":"argenis_perez@wvi.org","phone":"","role":"Asesor Regional","canal":"Discord"},
    {"client":"WV RD","name":"Juan Plata","email":"Juan_Plata@wvi.org","phone":"","role":"Atención al cliente","canal":"Discord"},
    # WV HN
    {"client":"WV HN","name":"Luis Gonzalez","email":"luis_gonzalez_rivera@wvi.org","phone":"+504 8992-7483","role":"Marketing Specialist","canal":"Discord y WP"},
    {"client":"WV HN","name":"Ruth Juarez","email":"ruth_juarez@wvi.org","phone":"","role":"Gerente Marketing y Comunicaciones","canal":"Correo"},
    {"client":"WV HN","name":"Andrea Medina","email":"andrea_medina@wvi.org","phone":"","role":"Specialist, Private Sector GAM-Grants Acquisition","canal":"Correo"},
    {"client":"WV HN","name":"Lucy Ramos","email":"lucymramos2001@gmail.com","phone":"","role":"","canal":"Correo"},
    {"client":"WV HN","name":"Abigail Gonzalez","email":"abigail_gonzalez@wvi.org","phone":"","role":"","canal":""},
    # WV ES
    {"client":"WV ES","name":"Isabel Iglesias","email":"Isabel_Iglesias@wvi.org","phone":"","role":"Marketing & Fundraising","canal":"Discord"},
    {"client":"WV ES","name":"Esther Solera","email":"Esther_Solera@wvi.org","phone":"","role":"Coordinadora de CRS y Donantes Estratégicos","canal":"Discord"},
    {"client":"WV ES","name":"Jesús Trejo","email":"Jesus_Trejo@wvi.org","phone":"","role":"Captación Digital","canal":"Discord"},
    {"client":"WV ES","name":"Jeison Peña","email":"jeison_pena@wvi.org","phone":"","role":"Captación Digital","canal":"Discord"},
    {"client":"WV ES","name":"Mario Gomez","email":"Mario_Gomez@wvi.org","phone":"","role":"Telemarketing","canal":"Discord"},
    {"client":"WV ES","name":"Nieves Carabana","email":"Nieves_Carabana@wvi.org","phone":"","role":"Iglesias","canal":"Discord"},
    {"client":"WV ES","name":"Vicente Aceituno","email":"Vicente_Aceituno@wvi.org","phone":"","role":"Finance Manager","canal":"Discord y Correo"},
    # WV Región
    {"client":"WV Región","name":"Jorge Girón","email":"jorge_giron@wvi.com","phone":"+504 3175-6818","role":"IT Business Partner, Global Technology & Digital Solutions","canal":"Discord y WP"},
    # WV CL
    {"client":"WV CL","name":"Gonzalo Macaya","email":"gonzalo_macaya@wvi.org","phone":"+56 9 6120 8842","role":"Gerente de Fundraising y Fidelización","canal":"Discord + Correo + WhatsApp"},
    {"client":"WV CL","name":"Diana Sanchez","email":"diana_sanchez@wvi.org","phone":"","role":"Coordinadora de Growth Marketing","canal":"Discord"},
    {"client":"WV CL","name":"Paola Pineda","email":"nidia_pineda@wvi.org","phone":"","role":"","canal":"Discord"},
    {"client":"WV CL","name":"Yesenia Soto","email":"yessenia_soto@wvi.org","phone":"","role":"Coordinadora de Telemarketing","canal":"Discord + Correo"},
    {"client":"WV CL","name":"Ornella Baldi","email":"ornella_baldi@wvi.org","phone":"","role":"Analista Comercial","canal":"Discord"},
    # WV BR
    {"client":"WV BR","name":"Rodrigo Flaire","email":"rodrigo_flaire@wvi.org","phone":"+55 11 91622 042","role":"Fundraising e Innovación","canal":"Correo + WhatsApp"},
    # WV EC
    {"client":"WV EC","name":"Johmara Vargas","email":"johmara_vargas@wvi.org","phone":"","role":"Coordinadora de Marketing & Fundraising","canal":"Discord"},
    {"client":"WV EC","name":"Juan Benalcazar","email":"juan_benalcazar@wvi.org","phone":"","role":"Coordinador Marketing Digital","canal":"Discord"},
    {"client":"WV EC","name":"Valeria Yanza","email":"martha_yanza@wvi.org","phone":"","role":"Analista de Cobranzas al Donante","canal":"Discord"},
    # WV PE
    {"client":"WV PE","name":"Alejandra Barcena","email":"alejandra_barcena_navarro@wvi.org","phone":"+51 948 706 384","role":"Coordinadora Nacional de Donantes Individuales","canal":"Correo"},
    {"client":"WV PE","name":"María Regalado","email":"maria_regalado_baldeon@wvi.org","phone":"","role":"Asistente de Atención y Fidelización al Donante","canal":"Correo"},
    {"client":"WV PE","name":"Aaron Mescco","email":"aaron_mescco_yupanqui@wvi.org","phone":"","role":"Analista de Afiliación y Cobranzas","canal":"Correo"},
    # WV CR
    {"client":"WV CR","name":"Rosy Arce","email":"rosy_arce@wvi.org","phone":"","role":"Supervisora de Marketing Digital y Comunicaciones","canal":"Discord"},
    # UCSP
    {"client":"UCSP","name":"Renzo Bravo","email":"rbravo@ucsp.edu.pe","phone":"+51 958 343 534","role":"Director de Marketing","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Cinthia Llaza","email":"cllaza@ucsp.edu.pe","phone":"+51 958 099 336","role":"Analista de Marketing","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Paolo Garate","email":"prgarate@ucsp.edu.pe","phone":"+51 991 581 900","role":"Analista Diseño Gráfico","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Romina Ampuero","email":"rampuero@ucsp.edu.pe","phone":"+51 980 730 973","role":"Auxiliar de Marketing","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Alonso Ugarte","email":"amugarte@ucsp.edu.pe","phone":"+51 932 122 285","role":"Jefe de Ventas Pregrado","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Fernando Herrera","email":"fmherrera@ucsp.edu.pe","phone":"+51 959 771 727","role":"Analista de Marketing Postgrado","canal":"WhatsApp + Correo"},
    {"client":"UCSP","name":"Pablo Gonzales","email":"prgonzales@ucsp.edu.pe","phone":"","role":"Director Centro de Idiomas","canal":"Correo"},
    {"client":"UCSP","name":"Claudia Tapia","email":"ctapiap@ucsp.edu.pe","phone":"","role":"Coordinadora de Marketing Digital","canal":"Correo + Discord"},
    {"client":"UCSP","name":"César Mogrovejo","email":"camogrovejo@ucsp.edu.pe","phone":"","role":"Analista de Marketing Digital","canal":"Correo + Discord"},
    # UPSJB
    {"client":"UPSJB","name":"Carlos Urquiaga","email":"CARLOS.URQUIAGA@UPSJB.EDU.PE","phone":"","role":"Director Comercial","canal":"Correo + Discord"},
    {"client":"UPSJB","name":"Estuardo Escobar","email":"ESTUARDO.ESCOBAR@UPSJB.EDU.PE","phone":"+51 986 886 825","role":"Jefe de Marketing","canal":"Correo + Discord"},
    {"client":"UPSJB","name":"Edgar Mendoza","email":"EDGARE.MENDOZA@upsjb.edu.pe","phone":"","role":"Gerente General","canal":"Correo + Discord"},
]

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
        if account == "General": account = current_account
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
        f.write("const TASKS = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("const TEAM_BN = " + json.dumps(TEAM_BN, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("const CLIENT_DIR = " + json.dumps(CLIENT_DIR, indent=2, ensure_ascii=False) + ";\n")
    print(f"Generated {output_path} successfully.")
