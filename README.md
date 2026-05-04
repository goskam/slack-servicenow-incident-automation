# Work in Progress

## Goal

Many teams waste time searching through documentation or handling simple incidents manually.

This project builds a Slack bot that gives quick access to AI directly in Slack. It can answer questions using documentation and help with common issues without needing to search for information.

It is powered by a local AI model (Mistral via Ollama), so everything runs locally.

The goal is to also automate simple incident responses in ServiceNow where possible, reducing manual work and speeding up support.

---

## Status

- Bot is connected to Slack using socket mode  
- It can receive messages and @mentions  
- Basic event handling is working locally (like app_mention)
- Messages are processed by a local AI model (Mistral served via Ollama) and sent to Slack

---

## Current Flow

Slack message → bot receives event → AI processes message → response is sent back to Slack  

---

## Next Steps

- Connect to internal documentation to improve AI understanding of incidents  
- Improve routing and classification of different request types  
- Integrate ServiceNow to automatically create and update incident tickets  
- Add automatic responses in ServiceNow for incoming incidents when resolution is simple  
- Improve response quality, structure, and consistency  