import sqlite3

def save_customer(db_path, customer):
    conn=sqlite3.connect(db_path)
    c=conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        job TEXT,
        income TEXT,
        work_year TEXT,
        software TEXT,
        receiver TEXT
    )
    ''')

    c.execute('''
    INSERT INTO customers
    (name,age,job,income,work_year,software,receiver)
    VALUES(?,?,?,?,?,?,?)
    ''',(
        customer['name'],
        customer['age'],
        customer['job'],
        customer['income'],
        customer['work_year'],
        customer['software'],
        customer['receiver']
    ))

    conn.commit()
    conn.close()
