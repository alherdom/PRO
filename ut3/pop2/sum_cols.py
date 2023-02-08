# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    i = 0
    sume = 0
    numbers = []
    with open(data_path,) as f:
        size = len(f.readline().split())

        f = open(data_path)
        lines = f.read().split()
        for element in lines:     
            print(lines[i])
            i += size
            if i == size*size:
                i = 0
                break
           


    csum = 0
    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')