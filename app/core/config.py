from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Redis Settings
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    # API Settings
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "CV Generation API"

    # CORS Settings
    BACKEND_CORS_ORIGINS: list = ["*"]

    # Storage Settings
    OUTPUT_DIR: str = "output"

    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
