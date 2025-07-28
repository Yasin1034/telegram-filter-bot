from telethon.sync import TelegramClient

api_id = 22821657
api_hash = 'a66819ce4aa6e70694b76021fffc5815'

client = TelegramClient('get_group_id', api_id, api_hash)

with client:
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        print(f"{dialog.name} - {dialog.id}")

"""indirim   -4916575543"""


"""deneme  -1002748069994"""