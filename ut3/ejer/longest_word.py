# ********************
# LA PALABRA M�S LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    with open(input_path, encoding="UTF-8") as f1:
        TRASH = ",.;:()"
        length = 0
        words = f1.read().split()
        for word in words:
            if len(word.strip(TRASH)) >= length:
                longest_word = word.strip(TRASH)
                length = len(word.strip(TRASH))
            
                

 

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')