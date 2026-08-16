import sqlite3
from config import DATABASE_PATH

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS images(id INTEGER PRIMARY KEY, path TEXT, md5 TEXT, phash TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT, job TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS collision_records(id INTEGER PRIMARY KEY, result TEXT)')

    conn.commit()
    conn.close()
