# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    i = 0
    count = 0
    colum_numbers = []
    with open(data_path,) as f:
        size = len(f.readline().split())

        f = open(data_path)
        lines = f.read().split()
        colum_numbers.append(lines[0])
        for line in lines:
            count += 1
            if count == size+1:
                colum_numbers.append(line)
                count = 1
        print(colum_numbers)


    csum = 0
    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')