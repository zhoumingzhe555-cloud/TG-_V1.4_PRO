import sqlite3
import os
from config import DATABASE_PATH

def init_db():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS images(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id TEXT,
        file_path TEXT,
        md5 TEXT UNIQUE,
        phash TEXT,
        customer_id INTEGER,
        submitter TEXT,
        created_time TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS collisions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        old_image_id INTEGER,
        new_file_id TEXT,
        score REAL,
        status TEXT,
        created_time TEXT
    )
    ''')

    conn.commit()
    conn.close()
