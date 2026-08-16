import os
import sqlite3
from config import DATABASE_PATH


def init_db():

    folder = os.path.dirname(DATABASE_PATH)

    if folder:
        os.makedirs(folder, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        job TEXT,
        income TEXT,
        software TEXT,
        receiver_type TEXT,
        receiver TEXT,
        submitter TEXT,
        chat_id TEXT,
        created_time TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        file_hash TEXT,
        phash TEXT,
        ai_feature TEXT,
        face_feature TEXT,
        file_path TEXT,
        created_time TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS collisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        old_submitter TEXT,
        new_submitter TEXT,
        score REAL,
        status TEXT,
        created_time TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT UNIQUE,
        title TEXT,
        created_time TEXT
    )
    ''')

    conn.commit()
    conn.close()

    print("数据库初始化完成")
