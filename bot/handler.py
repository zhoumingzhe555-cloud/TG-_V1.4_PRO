from ai.image_feature import check_ai_similarity

async def photo_handler(update, context):
    await update.message.reply_text(
        '🔍 检测结果\n\n系统正在检测图片'
    )
