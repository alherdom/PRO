# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    num_lines = num_words = num_bytes = 0
    with open(input_path) as f: #encoding="utf8"
        for line in f:
            num_lines += 1
            num_words += len(line.strip().split(" "))
            num_bytes += len(line.encode('utf-8')) 
    return num_lines, num_words, num_bytes
            


if __name__ == '__main__':
    run('data/wc/lorem.txt')