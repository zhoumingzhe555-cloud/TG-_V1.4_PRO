
import re


def parse_customer_info(text):

    data = {
        "name": "",
        "age": "",
        "job": "",
        "income": "",
        "work_year": "",
        "software": "",
        "receiver": ""
    }

    rules = {
        "name": ["姓名", "姓名:", "名字"],
        "age": ["年龄", "年齡"],
        "job": ["职业", "職業"],
        "income": ["收入"],
        "work_year": ["工作年限"],
        "software": ["引流软件", "引流軟件"],
        "receiver": ["接粉人员", "接粉人員"]
    }

    lines = text.splitlines()

    for line in lines:
        for key, words in rules.items():
            for word in words:
                if word in line:
                    value = line.replace(word, "")
                    value = value.replace(":", "").replace("：", "")
                    data[key] = value.strip()

    return data
