from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Production Template"
    environment: str = "development"
    database_url: str = "postgresql://portfolio:portfolio@postgres:5432/portfolio"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        extra="ignore",
    )


settings = Settings()
