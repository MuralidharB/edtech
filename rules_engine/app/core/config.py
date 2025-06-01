from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file at startup
load_dotenv()

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"  # fallback if load_dotenv isn't used

settings = Settings()

