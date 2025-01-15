import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")


sources = {-1001244605015: "@aviatorshina",
           -1001512563032: "@favt_ru",
           -1001638115755: "@gkovd_ru",
           -1001342511514: "@aviaincident",
           -1001313262929: "@ATOjournal",
           -1001436642859: "@inside_avia",
           -1001265775100: "@AviaCT",
           -1001449203159: "@antresol_avia",
           -1001148581454: "@frequentflyers",
           -1002178057836: "test"
           }
destination = -1002240708984


client = TelegramClient('avia_news', api_id, api_hash, system_version="4.16.30-vxCUSTOM")


# async def forward_message_to_destination(message):
#     # await client.forward_messages(destination, message)
#     await message.forward_to(destination)


@client.on(events.NewMessage(chats=sources))
async def forwarding_messages(message):
    try:
        if message.grouped_id:
            return    # ignore messages that are gallery here

        await asyncio.sleep(15)
        await message.forward_to(destination)
    except Exception as e:
        print(f"Не удалось отправить новость: {e}")


@client.on(events.Album(chats=sources))
async def forwarding_albums(event):
    try:
        await asyncio.sleep(15)
        await event.forward_to(destination)
    except Exception as e:
        print(f"Не удалось отправить альбом из новости: {e}")

with client:
    client.run_until_disconnected()
