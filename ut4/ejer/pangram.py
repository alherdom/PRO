# ********
# PANGRAMA
# ********


def is_pangram(text:str) -> bool:
    set_text = set(text)
    if len(set_text) >= 27:
        return True
    return False
    