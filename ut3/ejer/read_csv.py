# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    NUMBERS = ("1234567890")
    data = []
    key_line = []
    value_lines = []
    pokedex = {}
    i = 0
    with open(datafile) as f:
        key_line = f.readline().strip().split(",")
        for lines in f:
            value_lines = lines.strip().split(",")
            for value in value_lines:
                pokedex[key_line[i]] = value_lines[i]
                i += 1
                if i == 12:
                    i = 0
                if value in NUMBERS:
                    pokedex[key_line[i]] =int(value)
                if value == "False":
                    pokedex[key_line[-1]] = False
                if value == "True":
                    pokedex[key_line[-1]] = True
      
        data.append(pokedex)

      
        
                    
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')