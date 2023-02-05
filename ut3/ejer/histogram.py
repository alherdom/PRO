# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    frequencies = []
    with open(data_path) as f:
        letters = sorted(list(set(f.read())))
        data = open(data_path).read()
        for letter in letters:
            frequencies.append(data.count(letter))
    histogram_path = 'data/histogram/histogram.txt'
    with open(histogram_path, "w") as f:
        for letter, frequencie in zip(letters,frequencies):
            f.write(f'{letter} {frequencie*"█"} {frequencie}\n')

    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')