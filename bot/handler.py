import os
from datetime import datetime
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN
from core.duplicate import check_image, save_image


async def photo_handler(update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    tg_user = update.message.from_user.username or str(update.message.from_user.id)
    chat_id = str(update.message.chat.id)

    file = await context.bot.get_file(photo.file_id)

    os.makedirs("data/images", exist_ok=True)

    path = f"data/images/{photo.file_id}.jpg"

    await file.download_to_drive(path)

    result = check_image(path)

    if result:
        if result["type"] == "same":
text = (
    "⚠️ 撞客\n\n"
    "匹配类型：同一图片\n"
    "相似度：100%\n"
)
            )
        else:
            text = (
                "⚠️ 疑似撞客\n\n"
                f"图片相似度：{result['score']}%"
            )

        await update.message.reply_text(text)

    else:
        save_image(
            path,
            photo.file_id,
            tg_user,
            chat_id
        )

        await update.message.reply_text(
            "✅ 新客户\n\n"
            "图片已加入客户库"
        )


def start_bot():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.PHOTO, photo_handler)
    )

    print("Telegram图片监听启动")

    app.run_polling()
