# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    keys = {}
    values = []
    data = []
    with open(datafile) as f:
        for lines in f:
            keys = lines.strip().split(",")
            data = [keys]
            break
        for lines in f:
            values += lines.strip().split(",")
        for value in values:
            if value == 'False':
                values[-1] = False
                print(values[-1])
            elif value.isdigit():
                value = int(value)
                print(value)
        print(values)
        
                    
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')