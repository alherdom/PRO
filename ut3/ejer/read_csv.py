# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = {}
    with open(datafile) as f:
        for line in f:
            keys = line[0:12:1]
            print(keys)
            break

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')