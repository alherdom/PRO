# ********************
# LA PALABRA M�S LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    with open(input_path, encoding="UTF-8") as f1:
        TRASH = ",.;:()"
        length0 = 0
        words = f1.read().split()
        for word in words:
            length1 = len(word.strip(TRASH))
            if length1 >= length0:
                longest_word = word.strip(TRASH)
                length0 = length1
            
 

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')