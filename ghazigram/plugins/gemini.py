from ghazigram.core.gemini_client import gemini
from ghazigram.core.client import ghazigram
from telethon import events


class Gemini:
    print("Gemini plugin started.")
    @ghazigram.on(events.NewMessage(outgoing=True, pattern=r".gemini\s*(.+)"))
    async def gemini(event):
        query = event.pattern_match.group(1)
        try:
            response = gemini.send_message(query)
            await event.reply(response.text)
        except Exception as e:
            await event.reply(f"Your api key invalid please check.")