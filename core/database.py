
import sqlite3
import os
from config import DATABASE_PATH


def init_customer_table():

    folder = os.path.dirname(DATABASE_PATH)

    if folder:
        os.makedirs(folder, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)

    c = conn.cursor()

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
        ocr_text TEXT,
        created_time TEXT
    )
    """)

    conn.commit()
    conn.close()
