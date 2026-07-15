from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Yellow River GeoAgent"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"
    llm_provider: str = "mock"
    map_provider: str = "mock"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

