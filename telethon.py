from telethon import TelegramClient, sync, events
import json
import requests

# Вставляем api_id и api_hash
api_id = ''
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(from_users=['NAME_T']))
async def indicatum_handler(event):
    message = event.message.message
    print(message)

client.start()
client.run_until_disconnected()
