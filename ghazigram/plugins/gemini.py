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
            value = 4096
            value2 = 0
            while True:
                if len(response.text) > value:
                    await event.reply(response.text[value2:value])
                    value2 = value
                    value += 4096
                    if len(response.text) <= value:
                        break
                else:
                    await event.reply(response.text)
                    break
        except Exception as e:
            await event.reply(f"Your api key invalid please check.")