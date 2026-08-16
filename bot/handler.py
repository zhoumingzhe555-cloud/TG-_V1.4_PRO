import os

from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN

from core.duplicate import (
    check_image,
    save_image
)

from ocr.extractor import extract_text
from core.customer import parse_customer_info



# 判断是否有客户资料

def has_customer_info(text):

    if not text:
        return False


    keywords = [
        "姓名",
        "年齡",
        "年龄",
        "職業",
        "职业",
        "收入",
        "工作年限",
        "引流軟件",
        "引流软件",
        "接粉人員",
        "接粉人员"
    ]


    count = 0


    for word in keywords:

        if word in text:
            count += 1


    # 至少出现两个资料字段
    return count >= 2





async def photo_handler(
        update,
        context: ContextTypes.DEFAULT_TYPE
):


    photo = update.message.photo[-1]


    username = (
        update.message.from_user.username
        or str(update.message.from_user.id)
    )


    chat_id = str(
        update.message.chat.id
    )



    # 下载图片

    file = await context.bot.get_file(
        photo.file_id
    )


    os.makedirs(
        "data/images",
        exist_ok=True
    )


    path = (
        f"data/images/"
        f"{photo.file_id}.jpg"
    )


    await file.download_to_drive(
        path
    )



    # ==========================
    # OCR读取图片文字
    # ==========================

    try:

        ocr_text = extract_text(path)

    except Exception:

        ocr_text = ""




    # ==========================
    # 先检测撞客
    # ==========================

    result = check_image(path)



    if result:


        if result["type"] == "same":


            msg = (
                "🔍 检测结果\n\n"
                "🔴 撞客\n\n"
                "匹配类型：同一图片\n"
                "相似度：100%"
            )


        else:


            msg = (
                "🔍 检测结果\n\n"
                "🟠 疑似撞客\n\n"
                "匹配类型：相似图片\n"
                f"相似度：{result['score']}%"
            )


        await update.message.reply_text(
            msg
        )

        return




    # ==========================
    # 判断是否有客户资料
    # ==========================


    if has_customer_info(
        ocr_text
    ):


        customer = parse_customer_info(
            ocr_text
        )


        # 有资料，正式入库


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


    else:


        # =====================
        # 单图片模式
        # 只检测，不保存
        # =====================


        await update.message.reply_text(

            "🔍 检测结果\n\n"
            "恭喜您，是新客户"

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
