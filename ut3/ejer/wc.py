# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    num_lines = num_words = num_bytes = 0
    
    #---------LECTURA FICHERO. CALCULO DE LINEAS----------#
    with open(input_path) as f:
        for line in f:
            num_lines += 1
            for items in line:
                num_bytes +=1

    return num_lines, num_words, num_bytes

if __name__ == '__main__':
    run('data/wc/lorem.txt')