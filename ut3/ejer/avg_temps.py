# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    
    with open('data/avg_temps/temperatures.dat') as ftemps:
        for temp in ftemps:
            print(temp)
    
    with open('data/avg_temps/avg_temps.dat', 'w') as favg:
        for avg_temp in favg:
            favg.write(avg_temp)   
        
    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')