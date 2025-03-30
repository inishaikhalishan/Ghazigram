from gtts import gTTS
from telethon import events
from ghazigram.core.client import ghazigram
from ghazigram.utils.clean import Clean
from asyncio import sleep


class Gtts():
    def __init__(self, Audio_path):
        print("Text To Speech Plugin Started")
        @ghazigram.on(events.NewMessage(outgoing=True, pattern=".tts"))
        async def TTS(event):
                clear = Clean(Audio_path)
                message = event.message.text
                if event.is_reply:
                    get_message = await event.get_reply_message()
                    text = get_message.text
                    tts = gTTS(text)
                    tts.save(Audio_path) 
                    await ghazigram.send_file(event.chat_id, file=Audio_path, voice_note=True)
                    await event.delete()
                    await sleep(2)
                    clear.Clear()

                elif len(message) > 4:
                    tts = gTTS(message[4:len(message)])
                    tts.save(Audio_path)
                    await ghazigram.send_file(event.chat_id, file=Audio_path, voice_note=True)
                    await event.delete()
                    await sleep(2)
                    clear.Clear()
                else:
                    await event.respond("After entred the command, Then enter the message too.")
                    await event.delete()
