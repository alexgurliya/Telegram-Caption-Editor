from telegram import Bot
import configparser
import time
import os

# Load configuration
config = configparser.ConfigParser()
config.read("config.ini")

BOT_TOKEN = os.getenv("BOT_TOKEN", config["TELEGRAM"]["BOT_TOKEN"])
CHANNEL_ID = os.getenv("CHANNEL_ID", config["TELEGRAM"]["CHANNEL_ID"])
DELAY = int(os.getenv("DELAY", config["SETTINGS"]["DELAY"]))

# Define the posts to edit (message_id and new_caption)
POSTS_TO_EDIT = [
    {"message_id": 12345, "new_caption": "Updated Caption 1"},
    {"message_id": 12346, "new_caption": "Updated Caption 2"},
    {"message_id": 12347, "new_caption": "Updated Caption 3"},
]

def edit_captions():
    bot = Bot(token=BOT_TOKEN)
    for post in POSTS_TO_EDIT:
        try:
            bot.edit_message_caption(
                chat_id=CHANNEL_ID,
                message_id=post["message_id"],
                caption=post["new_caption"]
            )
            print(f"Caption updated for message_id: {post['message_id']}")
            time.sleep(DELAY)  # Respect Telegram's rate limits
        except Exception as e:
            print(f"Failed to edit message_id {post['message_id']}: {e}")

if __name__ == "__main__":
    edit_captions()
