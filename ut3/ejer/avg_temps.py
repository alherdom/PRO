# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    count = total = avgte = 0
    avg_temps = []
    
    #---------LECTURA FICHERO. CALCULO MEDIA----------#
    with open(input_path, 'r') as f:
        for line in f:
            month_temps = [int(t) for t in line.strip().split(',')]
            avg_temp = sum(month_temps) / len(month_temps)
            avg_temps.append(avg_temp)

            """
            line = line.strip().split(",")
            for temp in line:
                total += int(temp)
                count += 1
                if count == 31:
                    avgte = "{:.2f}".format(total / 31)
                    avg_temps.append(avgte)
                    count = total = 0
            """ 
    #-------------------SALIDA DE FICHERO-----------------#
    output_path = 'data/avg_temps/avg_temps.dat'
    with open('data/avg_temps/avg_temps.dat', 'w') as f:
        for avg_temp in avg_temps:
            f.write(f'{avg_temp:.2f}\n')    
        
    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')