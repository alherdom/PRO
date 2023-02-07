# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    
    
    with open(input_path) as f1:
        freq = {}
        words = f1.read().lower().split()
        for word in words:
            if words.count(word) >= lower_bound:
                freq[word] = words.count(word)
                
                
                
        output_path = 'data/common_words/output.txt'    
        with open(output_path, 'w') as f:
            f.write("Hola")
                  
    return filecmp.cmp(output_path, 'data/common_words/.expected', shallow=False)


if __name__ == '__main__':
    run('data/common_words/minizen.txt')