# Work in Progress

## Goal

Reduce manual effort in handling incidents and common support questions by combining Slack, ServiceNow, and a local AI model (Ollama).

The system provides AI responses in Slack and automatically forwards ServiceNow incidents to Slack channels.

---

## Current architecture

### ServiceNow → Slack (incident notifications)

ServiceNow incident created  
        ↓  
Business Rule / Scripted REST call  
        ↓  
FastAPI webhook (/servicenow/p1)  
        ↓  
Python processes payload  
        ↓  
Slack API sends message  
        ↓  
P1 Slack channel notification  

---

### Slack → AI assistant (Ollama)

User mentions bot in Slack (@IncidentBot)  
        ↓  
Slack Socket Mode event  
        ↓  
Python Slack Bolt handler  
        ↓  
Local AI model (Ollama / Mistral)  
        ↓  
Generated response  
        ↓  
Reply sent back in Slack thread  

---

## Status

- Slack bot connected via Socket Mode  
- AI responses from Ollama working via @mentions  
- FastAPI receives ServiceNow incident webhooks  
- ServiceNow P1 incidents are sent to Slack  
- Local environment uses ngrok for webhook exposure  

---

## Next steps

- Improve AI prompts for incident understanding  
- Add automatic incident classification (P1, P2, P3)  
- Connect internal documentation to AI responses  
- Add Slack commands for incident creation  
- Improve message formatting in Slack  
- Reduce manual steps in ServiceNow handling  