import os

from dotenv import load_dotenv

load_dotenv()

db_url = f"postgresql+asyncpg://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}"

redis_url = f"redis://{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}"
redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

secret = os.getenv("SECRET")
log_level = os.getenv("LOG_LEVEL")
hash = os.getenv("HASH")