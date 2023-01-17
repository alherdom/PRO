# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    letters = []
    for word in words:
        first_letter = word[0]
        if first_letter not in letters:
            letters.append(first_letter)
            group_words[first_letter] = word
    print(letters)
   
    
   
    """for letters, words in group_words.items():   
            if word.startswith(first_letter):
                group_words[letters] = words"""
   


    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])