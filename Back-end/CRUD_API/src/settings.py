import os
from dotenv import load_dotenv

load_dotenv(os.getenv('PATH_TO_ENV'))

class Settings:
    FIREBASE_DATABASE: str =  os.getenv('FIREBASE_DB') if os.getenv('FIREBASE_DB') else None
    MONGO_DATABASE: str =  os.getenv('MONGO_DB') if os.getenv('MONGO_DB') else None
    DB_PORT: str = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    LOGIN_API_URL: str = os.getenv("LOGIN_API_URL")
    ALLOW_ORIGINS: str = os.getenv("ALLOW_ORIGINS")
    ALLOW_CREDENTIALS: str = os.getenv("ALLOW_CREDENTIALS")
    ALLOW_METHODS: str = os.getenv("ALLOW_METHODS")
    ALLOW_HEADERS: str = os.getenv("ALLOW_HEADERS")
    PORT: int = os.getenv("HOST_PORT")
    HOST: str = os.getenv('HOST')
