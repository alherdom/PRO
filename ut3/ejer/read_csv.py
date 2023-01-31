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
                    value = False
                    print(value)
            
        print(keys)
        print(values)
  
        
                    
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')