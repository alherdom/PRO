# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = {}
    for char in sentence:
        if char in counter:
            continue
        counter[char] = sentence.count(char)
    return counter


if __name__ == '__main__':
    run('boom')
