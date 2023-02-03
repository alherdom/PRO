# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    # LECTURA DE FICHEROS. METO LAS MATRICES EN DOS LISTAS:
    with open(matrix1_path) as f1, open(matrix2_path) as f2:
        matrix1 = f1.read().split()
        matrix2 = f2.read().split()
        results = []
    # SUMO LAS DOS MATRICES MEDIANTE LA FUNCION ZIP:
        for values1, values2 in zip(matrix1, matrix2):
            results.append(int(values1)+int(values2))
    # ESCRIBO EL RESULTADO EL FICHERO DE SALIDA:
    result_path = 'data/sum_matrix/result.dat'
    with open(result_path, 'w') as fresult:
        count = 0         
        for result in results:
            if count != 4:
                fresult.write(f'{result} ')
                count += 1
            elif count >= 4:
                fresult.write(f'{result}\n')
                count = 0
    return filecmp.cmp(result_path, 'data/sum_matrix/.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')