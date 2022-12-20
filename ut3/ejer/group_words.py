# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    group_words = {}
    t_words = []
    first_letter = words[0][0]    
    for word in words:
        first_letter = word[0]
        group_words[first_letter] = t_words  
        
    for word in words:
        if word[0] in group_words:
            t_words.append(word)
            print(t_words)
        
      
        
    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])