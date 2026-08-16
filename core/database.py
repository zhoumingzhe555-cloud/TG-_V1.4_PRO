import os
import sqlite3

from config import DATABASE_PATH


def init_db():

    folder = os.path.dirname(DATABASE_PATH)

    if folder:
        os.makedirs(
            folder,
            exist_ok=True
        )


    conn = sqlite3.connect(
        DATABASE_PATH
    )

    c = conn.cursor()


    # 图片库
    c.execute("""
    CREATE TABLE IF NOT EXISTS images(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        file_id TEXT,

        file_path TEXT,

        md5 TEXT,

        phash TEXT,

        submitter TEXT,

        chat_id TEXT,

        ocr_text TEXT,

        created_time TEXT

    )
    """)



    # 客户资料库
    c.execute("""
    CREATE TABLE IF NOT EXISTS customers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        age TEXT,

        job TEXT,

        income TEXT,

        work_year TEXT,

        software TEXT,

        receiver TEXT,

        submitter TEXT,

        chat_id TEXT,

        created_time TEXT

    )
    """)


    conn.commit()

    conn.close()


    print(
        "数据库初始化完成"
    )



def init_customer_table():

    init_db()
