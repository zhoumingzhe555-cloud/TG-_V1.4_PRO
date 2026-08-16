from importer.parser import parse_customer

def scan_text(text):
    data=parse_customer(text)

    if data['name'] and any([
        data['age'],
        data['job'],
        data['income'],
        data['software'],
        data['receiver']
    ]):
        return data

    return None
