# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path
OPERATION_PATH = 'data/vending/operations.dat'
STATUS_PATH = 'data/vending/status.dat'

def run(operations_path: Path) -> bool:
    operations = []
    with open(OPERATION_PATH, encoding="utf8") as f1:
        for line in f1:
            line = line.strip().split()
            operations.append(line)
        for operation in operations:
            match operation[0]:
                
    
    
    # ESCRITURA SALIDA "STATUS"
    with open(STATUS_PATH, 'w', encoding="utf8") as f3:
        f3.write(f'Hola')

    return filecmp.cmp(STATUS_PATH, 'data/vending/.expected', shallow=False)


if __name__ == '__main__':
    run('data/vending/operations.dat')