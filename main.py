from core.database import init_db
from bot.app import start

if __name__ == '__main__':
    init_db()
    start()
