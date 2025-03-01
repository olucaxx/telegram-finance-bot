from unidecode import unidecode

def prep_str(data:str):
    return unidecode(data.strip().lower())

