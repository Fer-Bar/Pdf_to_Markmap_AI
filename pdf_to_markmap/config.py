from pydantic_settings import BaseSettings, SettingsConfigDict
from django.conf import settings


class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    DEBUG: bool = True
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=settings.BASE_DIR / ".env")

