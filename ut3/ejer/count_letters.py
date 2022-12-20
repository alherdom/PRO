# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    
    for char in sentence:
        if char in counter:
            continue
        amount_char = sentence.count(char)
        counter[char] = amount_char
    return counter


if __name__ == '__main__':
    run('boom')
