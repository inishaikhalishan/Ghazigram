from telethon import events
from ghazigram.core.client import ghazigram
from ping3 import ping


class Ping:
    print("ping plugin started.")
    @ghazigram.on(events.NewMessage(outgoing=True, pattern=".ping"))
    async def ping(event, host="google.com"):
        response_time = ping(host)
        if response_time is None:
            await event.reply("Ping Failed!")
        else:
            await event.reply(f"Ping: {response_time * 1000:2f} ms")