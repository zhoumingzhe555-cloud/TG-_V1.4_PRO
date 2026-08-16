import sqlite3
from config import DATABASE_PATH

def init_db():
    conn=sqlite3.connect(DATABASE_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT, submitter TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS images(id INTEGER PRIMARY KEY, customer_id INTEGER, file_hash TEXT, feature TEXT)')
    conn.commit()
    conn.close()
