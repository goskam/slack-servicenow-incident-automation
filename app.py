from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import SLACK_BOT_TOKEN, SLACK_APP_TOKEN

app = App(token=SLACK_BOT_TOKEN)

# register an event handler for when the bot is mentioned in Slack: @IncidentBot xyz
@app.event("app_mention")
def handle_message(event, say):

    print("handle_message function triggered")

    # raw event payload from Slack
    print("Event: ", event)

    # extract message text from the event
    text = event.get("text", "")

    print("DEBUG:", text)

    # send back a reply to same slack channel:
    say(f"Please follow steps below to solve your problem...")

if __name__ == "__main__":
    print("Connecting to Slack via Socket Mode")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    #listen for slack events
    handler.start()