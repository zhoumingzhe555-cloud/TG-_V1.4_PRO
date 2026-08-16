import hashlib
import sqlite3
from datetime import datetime

import imagehash
from PIL import Image

from config import DATABASE_PATH



def md5_file(path):

    h = hashlib.md5()

    with open(
        path,
        "rb"
    ) as f:

        h.update(
            f.read()
        )

    return h.hexdigest()



def get_phash(path):

    img = Image.open(path)

    return str(
        imagehash.phash(img)
    )





def check_image(path):


    md5 = md5_file(path)


    conn = sqlite3.connect(
        DATABASE_PATH
    )

    c = conn.cursor()



    # 完全相同图片

    c.execute(
        """
        SELECT id 
        FROM images
        WHERE md5=?
        """,
        (md5,)
    )


    row = c.fetchone()



    if row:


        conn.close()


        return {

            "type":"same",

            "image_id":row[0]

        }




    # 相似检测

    new_hash = get_phash(path)



    c.execute(
        """
        SELECT id,phash
        FROM images
        """
    )


    rows = c.fetchall()


    best_score = 0

    best_id = None



    for image_id, old_hash in rows:


        if old_hash:


            old = imagehash.hex_to_hash(
                old_hash
            )


            new = imagehash.hex_to_hash(
                new_hash
            )


            diff = old - new


            score = 100 - diff * 5



            if score > best_score:

                best_score = score

                best_id = image_id




    conn.close()



    if best_score >= 85:


        return {

            "type":"similar",

            "score":round(
                best_score,
                2
            ),

            "image_id":best_id

        }



    return None





def save_image(
        path,
        file_id,
        submitter,
        chat_id
):


    md5 = md5_file(path)

    phash = get_phash(path)



    conn = sqlite3.connect(
        DATABASE_PATH
    )

    c = conn.cursor()



    c.execute(
        """
        INSERT INTO images
        (
        file_id,
        file_path,
        md5,
        phash,
        submitter,
        chat_id,
        created_time
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            file_id,
            path,
            md5,
            phash,
            submitter,
            chat_id,
            datetime.now().isoformat()
        )
    )


    conn.commit()

    conn.close()
