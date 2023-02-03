# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    # TU C�DIGO AQU�

    return filecmp.cmp(histogram_path, 'data\histogram\.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')