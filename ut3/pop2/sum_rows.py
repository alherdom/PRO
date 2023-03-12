# *************
# SUMANDO FILAS
# *************
from pathlib import Path


def run(data_path: Path) -> tuple:
    # sume = 0
    # count = 0
    # sumes = []
    # with open(data_path,) as f:  
    #     for line in f:
    #         line = line.strip().split()
    #         for number in line:
    #             sume += int(number)
    #             count += 1
    #             if count == len(line):
    #                 sumes.append(sume)
    #                 count = 0
    #                 sume = 0       
    #     rsum = tuple(sumes)      
  
    rsum = []
    with open(data_path, 'r') as f:
        for row in f:
            numbers = []
            for n in row.strip().split():
                numbers.append(int(n))
            rsum.append(sum(numbers))
    rsum = tuple(rsum)
    return rsum


if __name__ == '__main__':
    run('data/sum_rows/data1.txt')