from telethon.sync import TelegramClient

api_id = 22821657      # kendi api_id
api_hash = 'a66819ce4aa6e70694b76021fffc5815'  # kendi api_hash

with TelegramClient('filter_session', api_id, api_hash) as client:
    print("Giriş tamamlandı.")