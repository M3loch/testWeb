from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def db_url():
        url : str = f"postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"
        return url
    

settings = Settings