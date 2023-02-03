# ********************
# LA PALABRA M�S LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    with open(input_path, encoding="UTF-8") as f1:
        TRASH = ",.;:()"
        size1 = 0
        words = f1.read().split()
        for word in words:
            size2 = len(word.strip(TRASH))
            if size2 >= size1:
                longest_word = word.strip(TRASH)
                size1 = size2
            
 

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')