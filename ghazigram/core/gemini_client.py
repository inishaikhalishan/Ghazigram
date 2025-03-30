from dotenv import load_dotenv
from os import environ

gemini = None

try:
    import google.generativeai as genai

    load_dotenv()


    api_key = environ["gemini_api"]


    genai.configure(api_key=api_key)

    gemini = genai.GenerativeModel("gemini-2.0-flash").start_chat()
except Exception:
        print("google-generativeai library is not installled.")
