#app.py

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN,SLACK_P1_CHANNEL_ID
from ai_service import ask_ollama
from fastapi import FastAPI, Request
import requests
import os
from slack_service import send_slack_message
import threading
import uvicorn



# slack bot workflow - tag a bot @IncidentBot -> get answer from Ollama in Slack
slack_app = App(token=SLACK_BOT_TOKEN)

# Deduplication store (in-memory) to prevent handling the same slack event multiple times (slow Ollama response)
processed_events = set()

# register an event handler for when the bot is mentioned in Slack: @IncidentBot xyz
@slack_app.event("app_mention")
def handle_message(event, say):

    # Deduplication - ignore duplicate Slack events (Slack may retry delivery because Ollama has slow response)
    event_id = event.get("event_ts")

    if event_id in processed_events:
        print("Ignoring duplicate event")
        return

    processed_events.add(event_id)

    # raw event payload from Slack (event)
    # print event type
    print("---Event triggered: ", event.get("type"))

    # extract message text from the event
    text = event.get("text", "")

    print("DEBUG:", text)

    ai_response = ask_ollama(text)

    # send back a reply to same slack channel:
    say(ai_response)

def run_slack():
    handler = SocketModeHandler(slack_app, SLACK_APP_TOKEN)
    handler.start()

#Service-now flow - create incident -> show notification on slack

api = FastAPI()

@api.get("/")
def health():
    return {"status": "running"}


@api.post("/servicenow/p1")
async def p1_event(request: Request):
    data = await request.json()

    message = (
        "*P1 INCIDENT*\n"
        f"Number: {data['number']}\n"
        f"Description: {data['short_description']}\n"
        f"Priority: {data['priority']}"
        f"Caller: {data.get('caller', 'unknown')}\n"
        f"Created by: {data.get('created_by', 'unknown')}"
    )

    send_slack_message(SLACK_P1_CHANNEL_ID, message)

    return {"status": "ok"}

#https://flatten-plug-amaze.ngrok-free.dev 

if __name__ == "__main__":

    # Slack runs in background
    threading.Thread(target=run_slack, daemon=True).start()

    # FastAPI runs in main thread
    uvicorn.run(api, host="127.0.0.1", port=8000)