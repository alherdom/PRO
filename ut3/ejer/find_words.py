# ***********************************
# �D�NDE EST�N LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list: 
    with open(data_path, encoding="UTF-8") as f:
        
        TRASH = "(,)'-¡!"
        target_word = target_word.lower()
        matches = []
        row = 0     
        for line in f:
            row += 1
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word.strip(TRASH) == target_word:
                    column = line.index(target_word) + 1
                    matches.append((row,column))
            if line.count(target_word) > 1:
                column = sum([i for i, e in enumerate(words) if e == target_word]) + len(words)* 2
                matches.append((row,column))
        for match in matches:
            if matches.count(match) > 1:
                matches.remove(match)
                    
                
                    
    return matches
    

if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')