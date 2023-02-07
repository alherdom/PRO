# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:

    with open(data_path,) as f:
        sumes = []
        count = 0
        size = len(f.readline().split())
        f = open(data_path, 'r')
        lines = f.read().split()
        sumes.append(lines[::3])
        
        print(sumes)
        
            
            
            
        
                            
                        
           
           
                 
        csum = 0


    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')