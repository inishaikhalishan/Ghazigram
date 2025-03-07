from ghazigram.core.client import ghazigram
from telethon.sync import TelegramClient
from ghazigram.plugins.tts import Gtts

audio_path = "assets/tts.mp3"

with ghazigram:

    TextToSpeech = Gtts(audio_path)


    ghazigram.run_until_disconnected()