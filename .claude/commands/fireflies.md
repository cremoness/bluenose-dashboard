# Skill: Fireflies.ai Integration

Eres un experto en la API de Fireflies.ai para el proyecto BlueNose Dashboard. Tu trabajo es ayudar a consultar, analizar e integrar datos de reuniones usando la API GraphQL de Fireflies.

## Contexto del Proyecto

- **Proyecto:** BlueNose Dashboard
- **Clientes activos:** UCSP, World Vision, UPSJB, VirtualPos/Chile, Smartimper, Caja Ica
- **Fuente de tareas:** `TASKS.md`
- **Dashboards:** `BlueNose_Dashboard.html`, `DailyBrief.html`, `STATUS_INTERNO.html`

## API de Fireflies.ai

### Endpoint
```
POST https://api.fireflies.ai/graphql
```

### Autenticación
```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

La API key se obtiene en: fireflies.ai → Integrations → Fireflies API → Copy Key

Para este proyecto, almacenarla como variable de entorno o en GitHub Secrets:
```
FIREFLIES_API_KEY=tu_api_key_aqui
```

---

## Queries GraphQL Principales

### 1. Listar todas las reuniones
```graphql
query {
  transcripts {
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
      shorthand_bullet
    }
  }
}
```

### 2. Obtener transcripción completa por ID
```graphql
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
      index
      speaker_name
      speaker_id
      text
      start_time
      end_time
    }
  }
}
```

### 3. Buscar reuniones por palabra clave
```graphql
query SearchMeetings($keyword: String!) {
  transcripts(title: $keyword) {
    id
    title
    date
    participants
    summary {
      overview
      action_items
    }
  }
}
```

### 4. Obtener analytics del speaker
```graphql
query {
  transcript(id: "TRANSCRIPT_ID") {
    title
    speakers {
      id
      name
      duration
      word_count
      words_per_min
      filler_word_count
    }
  }
}
```

---

## Ejemplos en Python (para daily_brief.py)

### Obtener action items de reuniones recientes
```python
import requests
import os

FIREFLIES_API_KEY = os.environ.get("FIREFLIES_API_KEY")

def get_recent_meetings(limit=5):
    query = """
    query {
      transcripts(limit: %d) {
        id
        title
        date
        participants
        summary {
          action_items
          overview
          keywords
        }
      }
    }
    """ % limit

    headers = {
        "Authorization": f"Bearer {FIREFLIES_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.fireflies.ai/graphql",
        json={"query": query},
        headers=headers
    )
    data = response.json()
    return data.get("data", {}).get("transcripts", [])


def get_action_items_for_brief():
    """Extrae action items de reuniones recientes para incluir en el brief diario."""
    meetings = get_recent_meetings(limit=3)
    action_items = []

    for meeting in meetings:
        title = meeting.get("title", "Reunión sin título")
        items = meeting.get("summary", {}).get("action_items", "")
        if items:
            action_items.append(f"📋 *{title}*\n{items}")

    return "\n\n".join(action_items) if action_items else "Sin action items recientes."
```

### Buscar reuniones por cliente
```python
def get_meetings_by_client(client_name):
    """Busca reuniones relacionadas a un cliente específico de BlueNose."""
    query = """
    query {
      transcripts(title: "%s") {
        id
        title
        date
        summary {
          overview
          action_items
        }
      }
    }
    """ % client_name

    headers = {
        "Authorization": f"Bearer {FIREFLIES_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.fireflies.ai/graphql",
        json={"query": query},
        headers=headers
    )
    return response.json().get("data", {}).get("transcripts", [])

# Uso por cliente BlueNose:
# get_meetings_by_client("UCSP")
# get_meetings_by_client("World Vision")
# get_meetings_by_client("UPSJB")
```

---

## Integración con el Daily Brief

Para enriquecer `daily_brief.py` con datos de Fireflies:

```python
def build_telegram_msg_with_fireflies():
    """Brief diario enriquecido con reuniones y action items de Fireflies."""
    # Tareas desde TASKS.md (lógica existente)
    tasks = parse_tasks()

    # Action items desde Fireflies
    action_items = get_action_items_for_brief()

    msg = f"""
📋 *Brief Diario BlueNose*

🔴 *Urgente:*
{tasks['urgent']}

🟡 *Esta semana:*
{tasks['weekly']}

🎙 *Action Items de Reuniones (Fireflies):*
{action_items}
"""
    return msg
```

---

## Límites y Consideraciones

| Plan | Requests/min | API Access |
|------|-------------|------------|
| Free / Pro | — | ❌ No disponible |
| Business | 60 req/min | ✅ Disponible |
| Enterprise | 60 req/min | ✅ Disponible |

- **Free/Pro:** 50 requests/día (sin acceso a API)
- **Business:** $29/usuario/mes — necesario para usar la API
- **Rate limit especial:** Add to Live API → 3 requests cada 20 minutos
- **Subir audio:** máximo 3,000 minutos/fuente/mes

---

## Flujo de Trabajo con BlueNose

Cuando el usuario pida tareas relacionadas a Fireflies, seguir este flujo:

1. **Verificar** que `FIREFLIES_API_KEY` está disponible como env var o en GitHub Secrets
2. **Identificar** qué datos necesita: transcripts, summaries, action items, speakers
3. **Construir** la query GraphQL apropiada
4. **Integrar** el resultado en TASKS.md, daily_brief.py, o los dashboards HTML según corresponda
5. **Mapear** clientes: UCSP, World Vision, UPSJB, VirtualPos, Smartimper, Caja Ica

## Comandos útiles para testear la API

```bash
# Test rápido de conexión
curl -X POST https://api.fireflies.ai/graphql \
  -H "Authorization: Bearer $FIREFLIES_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "query { transcripts(limit: 1) { id title date } }"}'
```

---

## Argumentos del comando

Puedes invocar esta skill con argumentos opcionales:

- `/fireflies` — Muestra opciones disponibles y estado de configuración
- `/fireflies transcripts` — Lista las últimas reuniones
- `/fireflies action-items` — Extrae action items recientes
- `/fireflies client UCSP` — Reuniones filtradas por cliente
- `/fireflies integrate` — Integra Fireflies con daily_brief.py

---

Cuando el usuario invoque esta skill, primero pregunta qué quiere hacer si no especificó argumentos: listar reuniones, extraer action items, buscar por cliente, o integrar con el dashboard/brief. Luego genera el código Python o la query GraphQL necesaria, adaptada al contexto de BlueNose.
