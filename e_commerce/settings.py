import os

from dotenv import load_dotenv

load_dotenv()

db_url = f"postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"
log_level = os.getenv("LOG_LEVEL")
redis_url = f"redis://{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}"
secret = os.getenv("SECRET")
hash = os.getenv("HASH")