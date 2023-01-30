# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    NUMBERS = "1234567890"
    data = []
    pokedex = {}
    values = []
    with open(datafile) as f:
        for lines in f:
            pokedex = lines.strip().split()
            break
        for lines in f:
            values += lines.strip().split()
            for value in values:
                if value in ('0123456789'):
                    
        
        print(pokedex)
        print(values)
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')