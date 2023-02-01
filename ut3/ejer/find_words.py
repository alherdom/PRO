# ***********************************
# �D�NDE EST�N LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    values = ()
    num_row = 0
    num_column = 0
    with open(data_path, 'r') as f:
        for line in f:
            num_row += 1
            list_words = line.strip().split()
            if target_word in line.strip():
                num_column = line.index(target_word) + 1
                print(num_row)
                print(num_column)
                break
        matches = [(num_row,num_column)]
            
    return matches
    

if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')