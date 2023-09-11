import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("DISCORD_APP_ID")
guild_id = os.getenv("DISCORD_GUILD_ID")
endpoint_url = (
    f"https://discord.com/api/v8/applications/{app_id}/guilds/{guild_id}/commands"
)
bot_token = os.getenv("DISCORD_BOT_TOKEN")

payload = {
    "name": "chatgpt",
    "description": "command for chatgpt",
    "options": [
        {"name": "message", "description": "message", "type": 3, "required": True}
    ],
}

response = requests.post(
    endpoint_url,
    json.dumps(payload),
    headers={"Authorization": f"Bot {bot_token}", "Content-Type": "application/json"},
)
print(response.text)
