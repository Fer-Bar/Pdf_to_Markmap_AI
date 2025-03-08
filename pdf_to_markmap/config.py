from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


@lru_cache
def get_settings():
    return Settings()


class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    DEBUG: bool = True
    SECRET_KEY: str
    FIREBASE_BUCKET_NAME: str
    FIREBASE_CREDENTIALS: str
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")


