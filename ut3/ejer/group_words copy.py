# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    first_letter = words[0][0]
    m = []
    b = []
    c = []
    a = []
    for word in words:
        first_letter = word[0]
        group_words[first_letter] = []

        if word.startswith('m'):
            m.append(word)
        if word.startswith('b'):
            b.append(word)
        if word.startswith('c'):
            c.append(word)
        if word.startswith('a'):
            a.append(word)
        
    group_words['m'] = m
    group_words['b'] = b
    group_words['c'] = c
    group_words['a'] = a
 






    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])