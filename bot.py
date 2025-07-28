from telethon import TelegramClient, events
import requests
import asyncio

api_id = 22821657
api_hash = 'a66819ce4aa6e70694b76021fffc5815'
bot_token = '7960080315:AAHlHfb9_RaBeocMIwMroGAS5faW-B0cpus'

target_chat = -1002833730183
source_group = 'onual_firsat'

keywords = ['Telefon', 'Bilgisayar', 'Tablet', 'Samsung', 'Apple', 'Xiaomi', 'Xıaomı', 'Powerbank',
            'Airpods', 'Kulaklık', 'Hoparlör', 'Televizyon', 'Led', 'Ram', 'Harddisk', 'Mouse',
            'Klavye', 'Monitör', 'Pc', 'Laptop', 'Dizüstü', 'Şarj']

client = TelegramClient('filter_session', api_id, api_hash)


@client.on(events.NewMessage(chats=source_group))
async def message_handler(event):
    message = event.message.message
    print(f"🔔 Yeni mesaj: {message}")

    if any(keyword.lower() in message.lower() for keyword in keywords):
        print("✔️ Filtreye uyan mesaj bulundu, bot ile gönderiliyor.")
        try:
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                'chat_id': target_chat,
                'text': f"🚨🔍 Filtreye uyan mesaj:\n\n{message}",
                'disable_notification': False
            }
            response = requests.post(bot_api_url, data=payload)
            response.raise_for_status()
            print("✅ Bot mesajı gönderdi.")
        except requests.RequestException as e:
            print(f"❌ Hata oluştu: {e}, response: {response.text}")


async def main():
    await client.connect()
    if not await client.is_user_authorized():
        print("❌ Oturum açık değil. Lütfen terminalden bir kez giriş yap.")
        return

    print("👂 Dinleme başladı...")

    try:
        bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': target_chat,
            'text': '✅ Bot başarıyla başlatıldı!',
            'disable_notification': False
        }
        response = requests.post(bot_api_url, data=payload)
        response.raise_for_status()
        print("✅ Başlangıç mesajı gönderildi.")
    except requests.RequestException as e:
        print(f"❌ Başlangıç mesajı hatası: {e}, response: {response.text}")

    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())



"""from telethon import TelegramClient, events
import requests
import asyncio

api_id = 22821657
api_hash = 'a66819ce4aa6e70694b76021fffc5815'
bot_token = '7960080315:AAHlHfb9_RaBeocMIwMroGAS5faW-B0cpus'

# Chat ID’yi buraya gir (-100 ile başlıyorsa eksiksiz gir)
target_chat = -1002833730183
source_group = 'onual_firsat'

keywords = ['Telefon', 'Bilgisayar', 'Tablet', 'Samsung', 'Apple', 'Xiaomi', 'Xıaomı', 'Powerbank', 'Airpods', 'Kulaklık', 'Hoparlör', 'Televizyon', 'Led', 'Ram', 'Harddisk', 'Mouse', 'Klavye', 'Monitör', 'Pc', 'Laptop', 'Dizüstü', 'Şarj']
""""""keywords = ['a']""""""

client = TelegramClient('filter_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def message_handler(event):
    message = event.message.message
    print(f"🔔 Yeni mesaj: {message}")

    if any(keyword.lower() in message.lower() for keyword in keywords):
        print("✔️ Filtreye uyan mesaj bulundu, bot ile gönderiliyor.")
        try:
            bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                'chat_id': target_chat,
                'text': f"🚨🔍 Filtreye uyan mesaj:\n\n{message}",
                'disable_notification': False
            }
            response = requests.post(bot_api_url, data=payload)
            response.raise_for_status()
            print("✅ Bot mesajı gönderdi.")
        except requests.RequestException as e:
            print(f"❌ Hata oluştu: {e}, response: {response.text}")

async def main():
    await client.start()
    print("👂 Dinleme başladı...")

    # Başlangıç mesajı
    try:
        bot_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': target_chat,
            'text': '✅ Bot başarıyla başlatıldı!',
            'disable_notification': False
        }
        response = requests.post(bot_api_url, data=payload)
        response.raise_for_status()
        print("✅ Başlangıç mesajı gönderildi.")
    except requests.RequestException as e:
        print(f"❌ Başlangıç mesajı hatası: {e}, response: {response.text}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

"""


"""from telethon import TelegramClient, events
import asyncio

api_id = 22821657
api_hash = 'a66819ce4aa6e70694b76021fffc5815'
group_chat_id = -4916575543
group_username = 'onual_firsat'


keywords = ['Telefon', 'Pc', 'Laptop', 'Bilgisayar', 'Tablet', 'Samsung', 'Powerbank', 'Dizüstü', 'Şarj', 'Ram', 'Mouse']


client = TelegramClient('filter_session', api_id, api_hash)

@client.on(events.NewMessage(chats=group_username))
async def handler(event):
    message = event.message.message
    if any(keyword.lower() in message.lower() for keyword in keywords):
        await client.send_message(group_chat_id, f"🚨🔍 Filtreye uyan mesaj:\n\n{message}", silent=False)

async def main():
    await client.start()
    print("Bot çalışıyor... Ctrl+C ile durdurabilirsin.")

    # Burada test mesajı gönderiyoruz
    await client.send_message(group_chat_id, "deneme mesajıdır.", silent=False)

    # Botu sürekli çalışır halde tutuyoruz
    await client.run_until_disconnected()

asyncio.run(main())
"""