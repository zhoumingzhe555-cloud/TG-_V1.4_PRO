import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from core.duplicate import check_image


async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    file = await context.bot.get_file(photo.file_id)

    os.makedirs("data/images", exist_ok=True)

    path = f"data/images/{photo.file_id}.jpg"

    await file.download_to_drive(path)

    result = check_image(path)

    if result:
        await update.message.reply_text(result)
    else:
        await update.message.reply_text(
            "✅ 图片已收到，进入客户检测流程"
        )


def start_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.PHOTO, photo_handler)
    )

    print("Telegram图片监听启动")

    app.run_polling()
