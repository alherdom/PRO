# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    with open(input_path, encoding="UTF-8") as f1:
        freq = {}
        words = f1.read().lower().split()
        freq = {word:words.count(word) for word in words if words.count(word) >= lower_bound}

        """for word in words:
            if words.count(word) >= lower_bound:
                freq[word] = words.count(word)"""
                


    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)