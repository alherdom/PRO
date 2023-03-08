# ********
# PANGRAMA
# ********


def is_pangram(text:str) -> bool:
    text = text.replace(' ','')
    if len(set(text)) >= 26:
        return True
    return False
    