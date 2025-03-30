import google.generativeai as genai
from dotenv import load_dotenv
from os import environ



load_dotenv()


api_key = environ["gemini_api"]


genai.configure(api_key=api_key)

gemini = genai.GenerativeModel("gemini-2.0-flash").start_chat()