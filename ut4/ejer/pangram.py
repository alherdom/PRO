# ********
# PANGRAMA
# ********


def is_pangram(text:str) -> bool:
    count = 0
    text = text.replace(" ","")
    if len(text) < 26 and count < 20:
        return False
    for char1, char2 in zip(text, text[1::]):
        if char1 == char2:
            count += 1
    return True
    