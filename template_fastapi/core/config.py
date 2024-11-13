from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App config
    APP_NAME: str = 'FastAPI Template'
    APP_VERSION: str = '0.1.0'
    APP_DESCRIPTION: str = 'FastAPI Template Description'

    # Database config
    DATABASE_URL: str = 'sqlite:///./database.db'

    # Security config
    SECRET_KEY: str = 'SECRET_KEY'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_DAYS: int = 1

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
