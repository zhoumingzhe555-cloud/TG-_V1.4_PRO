import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "/app/data/customers.db"
)
