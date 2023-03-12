# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    data = [line.strip().split() for line in open(data_path)]
    cols = []
    for col_index in range(len(data[0])):
        col = []
        for row_index in range(len(data)):
            num_in_col = data[row_index][col_index]
            col.append(int(num_in_col))
        cols.append(col)
    csum = tuple([sum(col) for col in cols])
    
    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')