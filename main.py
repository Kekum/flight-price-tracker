import os
import requests


def send_test_message():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": "✅ Flight Tracker çalışıyor."
        },
        timeout=30
    )

    response.raise_for_status()


if __name__ == "__main__":
    send_test_message()
