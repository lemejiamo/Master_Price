import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    PORT = int(os.getenv("PORT", 8080))
    FIREBASE_URL_ONE = os.getenv("FIREBASE_URL_ONE")
    LOGIN_API_URL = os.getenv("LOGIN_API_URL")

    ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS")
    ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS")
    ALLOW_METHODS = os.getenv("ALLOW_METHODS")
    ALLOW_HEADERS = os.getenv("ALLOW_HEADERS")
