from telegram.ext import Application, MessageHandler, filters
from config import BOT_TOKEN
from bot.handler import photo_handler

def start():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    print('V1.5 Final 商业版启动')
    app.run_polling()
