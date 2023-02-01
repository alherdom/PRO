# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open (datafile) as f:
        NUMBERS="1234567890"
        data=[]
        pokedex = {}
        i = 0
        for lines in f:
            key_line = line.strip().split(",")
            value_lines = lines.strip().split(",")
            print(key_line)
            print(value_lines)
            for value in value_lines:
                pokedex[key_line[i]] = value
                i += 1
                if i == 12:
                    i = 0
                    continue
        data.append(pokedex)
                    
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')