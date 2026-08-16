import json
from importer.scanner import scan_text

def import_json(path):
    result=[]

    with open(path,'r',encoding='utf-8') as f:
        data=json.load(f)

    for msg in data.get('messages',[]):
        text=msg.get('text','')

        if isinstance(text,list):
            text=''.join(
                str(x.get('text','')) if isinstance(x,dict) else str(x)
                for x in text
            )

        customer=scan_text(text)

        if customer:
            result.append(customer)

    return result
