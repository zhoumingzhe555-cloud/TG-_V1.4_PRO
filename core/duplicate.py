import hashlib
import sqlite3
import imagehash
from PIL import Image
from config import DATABASE_PATH


def md5_file(path):
    h = hashlib.md5()
    with open(path,'rb') as f:
        h.update(f.read())
    return h.hexdigest()


def get_phash(path):
    return str(imagehash.phash(Image.open(path)))


def check_image(path):

    md5 = md5_file(path)
    phash = get_phash(path)

    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()

    c.execute("SELECT id FROM images WHERE md5=?", (md5,))
    same = c.fetchone()

    if same:
        conn.close()
        return {
            "type":"same",
            "score":100,
            "image_id":same[0]
        }

    c.execute("SELECT id,phash FROM images")
    rows = c.fetchall()

    best = 0
    best_id = None

    for row in rows:
        if row[1]:
            old = imagehash.hex_to_hash(row[1])
            new = imagehash.hex_to_hash(phash)
            score = 100 - (old-new)*5
            if score > best:
                best = score
                best_id = row[0]

    conn.close()

    if best >= 85:
        return {
            "type":"similar",
            "score":best,
            "image_id":best_id
        }

    return None
