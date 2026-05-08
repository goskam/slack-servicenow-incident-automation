#slack_service.py

import requests
from config import SLACK_BOT_TOKEN

def send_slack_message(channel_id, message):
    url = "https://slack.com/api/chat.postMessage"

    payload = {
        "channel": channel_id,
        "text": message
    }

    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print("Slack response: ", response.json())

    return response.json()