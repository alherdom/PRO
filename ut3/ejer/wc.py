# ****************
# CONTANDO COMO WC
# ****************
from pathlib import Path


def run(input_path: Path) -> tuple:
    num_lines = num_words = num_bytes = 0
    
    #---------LECTURA FICHERO. CALCULO DE LINEAS----------#
    with open(input_path) as f:
        num_lines = sum(1 for line in f)
        print(num_lines)
    
    return num_lines, num_words, num_bytes

if __name__ == '__main__':
    run('data\wc\lorem.txt')