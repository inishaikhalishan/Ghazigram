from ghazigram.core.client import ghazigram
from ghazigram.plugins.gemini import Gemini
from telethon.sync import TelegramClient
from ghazigram.plugins.tts import Gtts
from ghazigram.plugins.ping import Ping

audio_path = "assets/tts.mp3"

with ghazigram:
    TextToSpeech = Gtts(audio_path)
    Gemini()
    Ping()
    ghazigram.run_until_disconnected()