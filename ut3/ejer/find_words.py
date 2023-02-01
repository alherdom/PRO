# ***********************************
# �D�NDE EST�N LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    matches = []
    values = ()
    num_row = num_column = 0
    trash = ".,;:()!¿'"
    with open(data_path, 'r') as f:
        for line in f:
            line = line.lower()
            num_row += 1         
            list_words = line.lower().strip().split()
            target_word = target_word.lower()  
            its_here = False
            num_times = list_words.count(target_word)
            if num_times == 2:
                print(target_word)
                num_column = line.index(target_word) + 1
                values = (num_row,num_column)
                matches.append(values)

        #USO EL "if" Y UN BOOLEANO PARA SABER SI LA PALABRA ESTÁ ÚNICAMENTE EN LA LISTA
            for word in list_words:
                word = word.strip(trash)
                if word == target_word:
                    its_here = True
        #USO "in" PARA SABER SI LA PALABRA ESTA EN LA LINEA        
            if target_word in line.strip() and its_here:
                    num_column = line.index(target_word) + 1
                    values = (num_row,num_column)
                    matches.append(values)
       
    return matches
    

if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')