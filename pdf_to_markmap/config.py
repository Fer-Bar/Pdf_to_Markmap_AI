from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    DEBUG: bool = True

    model_config = SettingsConfigDict(env_file="../.env")


try:
    settings = Settings()
except ValidationError as e:
    print("Error en la configuración:", e)
    settings = None
