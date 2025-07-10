from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()
import os

class Settings(BaseSettings):
    database_url: str = os.getenv('DATABASE_URL')
    secret_key: str = os.getenv("SECRET_KEY")

settings = Settings()