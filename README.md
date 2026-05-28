# OpenAI Basics & AI Integration Projects

Dieses Repository dokumentiert meinen Lernweg im Bereich AI Integration, AI Automation und Workflow Engineering mit Python und der OpenAI API.

Der Fokus liegt auf:
- praktischen Projekten
- echter API Integration
- sauberer Softwarestruktur
- Git/GitHub Workflows
- modernen AI Automation Use Cases

---

# Technologien

- Python
- OpenAI API
- JSON
- Git & GitHub
- VS Code

---

# Projekte

## AI Email Classifier

Ein CLI Tool zur automatischen Analyse und Kategorisierung von Kundenemails mit der OpenAI API.

### Features

- OpenAI API Integration
- strukturierte JSON Outputs
- AI Email Analyse
- Prioritätsbewertung
- Kategorien-Erkennung
- Error Handling mit try/except
- dynamische User Inputs
- wiederverwendbare Funktionen
- modulare Code-Struktur mit main()

### Beispiel Output

```json
{
  "category": "abrechnung",
  "priority": "hoch",
  "summary": "Kunde hat trotz Zahlung eine Mahnung erhalten.",
  "suggested_reply": "Vielen Dank für Ihre Nachricht. Wir prüfen den Vorgang schnellstmöglich."
}
```

---

## AI News Summarizer

Ein CLI Tool zur automatischen Analyse und Zusammenfassung von News-Artikeln mit der OpenAI API.

### Features

- OpenAI API Integration
- strukturierte JSON Outputs
- AI News Analyse
- Sentiment Analyse
- Kategorien-Erkennung
- Zusammenfassungen in 2–3 Sätzen
- TLDR Kurzfassung
- Key Point Extraktion
- Error Handling mit try/except
- dynamische User Inputs
- wiederverwendbare Funktionen über utils.py
- modulare Code-Struktur mit main()

### Beispiel Output

```json
{
  "category": "Wirtschaft",
  "sentiment": "neutral",
  "summary": "Die Europäische Zentralbank hat beschlossen, die Zinssätze vorerst nicht zu ändern. Analysten sehen jedoch weiterhin wirtschaftliche Unsicherheiten.",
  "key_points": [
    "Die EZB hält die Zinssätze stabil.",
    "Analysten erwarten weitere Unsicherheiten.",
    "Die wirtschaftliche Entwicklung bleibt unklar."
  ],
  "tldr": "Die EZB belässt die Zinssätze stabil trotz wirtschaftlicher Unsicherheiten."
}
```
---

# Lernfokus

Dieses Repository dient als praktisches Lern- und Portfolio-Repository mit Fokus auf:

- AI Integration
- strukturierte AI Outputs
- API Workflows
- Python Softwarestruktur
- Backend Grundlagen
- AI Automation

---

# Roadmap

Geplante nächste Projekte:

- AI News Summarizer
- Telegram / Discord AI Bot
- AI Ticket Routing System
- FastAPI Backend Projekte
- AI Workflow Automationen

---

# Ziel

Ziel ist der Aufbau praxisnaher Fähigkeiten für Rollen wie:

- Junior AI Integration Engineer
- AI Automation Developer
- AI Workflow Engineer

mit Fokus auf:
- Python
- APIs
- Automationen
- strukturierte AI Systeme
- reale Business Use Cases