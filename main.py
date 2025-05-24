from telethon import TelegramClient, events

APP_ID = 123
APP_HASH = "A1B2C3D4E5F6"
SESSION_PATH = "/storage/emulated/0/temp/tochno_moy_akkaunt.session"
client = TelegramClient(SESSION_PATH, APP_ID, APP_HASH)

@client.on(events.NewMessage(chats=[777000]))
async def message_handler(event):
    print(f"\n{event.raw_text}")

client.start(); client.run_until_disconnected()

# положить: CTRL+C