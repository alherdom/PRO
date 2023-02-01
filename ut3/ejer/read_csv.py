# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open (datafile) as f:
        NUMBERS="1234567890"
        data=[]
        pokedex = {}
        first_line = f.readline()
        i = 0
        for lines in f:
            key_line = first_line.strip().split(",")
            value_lines = lines.strip().split(",")
            for value in value_lines:
                if value[0] in NUMBERS:
                     pokedex[key_line[i]] = int(value)
                     i += 1
                elif value=="False":
                    pokedex[key_line[i]] = False
                    i += 1
                elif value=="True":
                    pokedex[key_line[i]] = True
                    i += 1
                else:
                    pokedex[key_line[i]] = value
                    i += 1
            i=0
            data.append(pokedex)
                    
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')