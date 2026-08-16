ocr_text = extract_text(path)

if 判断有客户资料:

    # 检测撞客
    result = check_image(path)

    if result:
        返回撞客
    else:
        save_image()
        返回：
        "✅ 新客户\n\n新客户已加入客户库"

else:

    # 单纯图片查询
    result = check_image(path)

    if result:
        返回撞客
    else:
        返回：
        "🔍 检测结果\n\n恭喜您，是新客户"

    # 不执行 save_image()
