# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    block = "█"
    LETTERS = "ABCDEFGH"
    numbers = []
    with open(data_path) as f1:
        data = f1.read()
        for letter in LETTERS:
            numbers.append(data.count(letter))

    histogram_path = 'data/histogram/histogram.txt'
    with open(histogram_path, "w") as fhistogram:
        for key, value in zip(LETTERS, numbers):
            fhistogram.write(f'{key} {value*block} {value}\n')
    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')