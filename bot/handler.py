import os
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN
from core.duplicate import check_image, save_image


async def photo_handler(update, context: ContextTypes.DEFAULT_TYPE):

    photo = update.message.photo[-1]

    # 提交人
    username = (
        update.message.from_user.username
        or str(update.message.from_user.id)
    )

    # 群ID
    chat_id = str(update.message.chat.id)


    # 下载图片

    file = await context.bot.get_file(photo.file_id)


    os.makedirs(
        "data/images",
        exist_ok=True
    )


    path = (
        f"data/images/"
        f"{photo.file_id}.jpg"
    )


    await file.download_to_drive(path)



    # 图片检测

    result = check_image(path)



    if result:


        # 完全一样

        if result["type"] == "same":


            text = (
                "🔴 撞客\n\n"
                "匹配类型：同一图片\n"
                "相似度：100%"
            )


        # 相似图片

        else:


            text = (
                "🟠 疑似撞客\n\n"
                "匹配类型：相似图片\n"
                f"相似度：{result['score']}%\n\n"
                "请人工确认"
            )


        await update.message.reply_text(text)


    else:


        # 新图片入库

        save_image(
            path,
            photo.file_id,
            username,
            chat_id
        )


        await update.message.reply_text(
            "✅ 新客户\n\n"
            "新客户已加入客户库"
        )





def start_bot():


    app = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )


    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            photo_handler
        )
    )


    print(
        "Telegram图片监听启动"
    )


    app.run_polling()
