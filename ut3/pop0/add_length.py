# *********************
# PALABRAS CON LONGITUD
# *********************


def run(text: str) -> list:
    text = text.split()
    words_length = []
    for words in text:
        size = len(words)
        parts = f'{words} {size}'
        words_length.append(parts)
    return words_length


if __name__ == '__main__':
    run('todo se transforma')
