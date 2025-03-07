from os import environ
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession


load_dotenv()

class Ghazigram():
    def __init__(self):
        self.api_id = environ["api_id"]
        self.api_hash = environ["api_hash"]
        self.string_session = environ["string_session"]
        self.client = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)


ghazigram = Ghazigram().client