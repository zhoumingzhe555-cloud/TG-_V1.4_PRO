import sqlite3
from datetime import datetime
from config import DATABASE_PATH


def save_customer(data, submitter="", chat_id=""):

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

        submitter TEXT,
        chat_id TEXT,

        created_time TEXT
    )
    """)


    c.execute("""
    INSERT INTO customers
    (
        name,
        age,
        job,
        income,
        work_year,
        software,
        receiver,
        submitter,
        chat_id,
        created_time
    )

    VALUES(?,?,?,?,?,?,?,?,?,?)

    """,
    (
        data.get("name"),
        data.get("age"),
        data.get("job"),
        data.get("income"),
        data.get("work_year"),
        data.get("software"),
        data.get("receiver"),
        submitter,
        chat_id,
        datetime.now().isoformat()
    ))


    conn.commit()

    conn.close()
