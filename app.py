from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN
from ai_service import ask_ollama

app = App(token=SLACK_BOT_TOKEN)

# Deduplication store (in-memory) to prevent handling the same slack event multiple times (slow Ollama response)
processed_events = set()

# register an event handler for when the bot is mentioned in Slack: @IncidentBot xyz
@app.event("app_mention")
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

if __name__ == "__main__":
    print("Connecting to Slack via Socket Mode")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    #listen for slack events
    handler.start()