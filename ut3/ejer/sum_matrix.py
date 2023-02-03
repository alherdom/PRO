# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    with open(matrix1_path, encoding="UTF-8") as f1, open(matrix2_path, encoding="UTF-8") as f2:
        readm1 = f1.read()   
        matrix1 = readm1.split()
        readm2 = f2.read()   
        matrix2 = readm2.split()
        results = []
        for values1, values2 in zip(matrix1, matrix2):
            results.append(int(values1)+int(values2))
    result_path = 'data/sum_matrix/result.dat'
    with open(result_path, 'w') as fresult:
        count = 0
        for result in results:
            count += 1
            fresult.write(f'{result} ')
            if count == 5:
                fresult.write(f'\n')
                count = 0
    
    
    
    
    return filecmp.cmp(result_path, 'data\sum_matrix\.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')