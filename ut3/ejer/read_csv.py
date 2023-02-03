# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    with open (datafile) as f:
        data=[]
        firstline = f.readline().strip().split(",")
        for lines in f:
            pokedex = {}
            value_lines = lines.strip().split(",")
            for key, value in zip(firstline, value_lines):
                if value.isdigit():
                    value = int(value)
                elif value == "False":
                    value = False
                elif value == "True":
                    value = True
                pokedex[key] = value
            data.append(pokedex)
                
        
     
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')