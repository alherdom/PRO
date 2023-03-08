# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words: list) -> tuple:
    lower_words = [word for word in words if word.islower()]
    upper_words = [word for word in words if word.isupper()]
    return (lower_words,upper_words)

    # lower_words = []
    # upper_words = []
    # for word in words:
    #     if word.islower():
    #         lower_words.append(word)
    #     elif word.isupper():
    #         upper_words.append(word)
    # return (lower_words,upper_words)