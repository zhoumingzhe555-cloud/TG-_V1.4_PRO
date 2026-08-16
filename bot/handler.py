import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

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

        if result["type"] == "same":
            msg = (
                "⚠️ 发现历史图片\n\n"
                "匹配类型：同一图片\n"
                "相似度：100%"
            )

        else:
            msg = (
                "⚠️ 疑似撞客\n\n"
                f"图片相似度：{result['score']}%"
            )

        await update.message.reply_text(msg)

    else:

        await update.message.reply_text(
            "✅ 图片已收到\n正在检测客户"
        )


def start_bot():

    app = Application.builder()\
        .token(BOT_TOKEN)\
        .build()


    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            photo_handler
        )
    )


    print("Telegram图片监听启动")

    app.run_polling()
