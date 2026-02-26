# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # PostgreSQL credentials
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # Optional: FastAPI settings
    APP_NAME: str = "Banking LMS"
    DEBUG: bool = True

    @property
    def DATABASE_URL(self) -> str:
        # URL-encode special chars like @ in password
        from urllib.parse import quote_plus
        password = quote_plus(self.POSTGRES_PASSWORD)
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{password}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

# Load from .env automatically
settings = Settings(_env_file=".env")