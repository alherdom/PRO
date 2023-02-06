# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path
def run(route_path: Path) -> tuple:
    MIN_DEPTH = distance = depth = 0
    MAX_DEPTH = 600
    LPM = 3
    with open(route_path) as f:
        fuel = int(f.readline())
        moves = f.readline().strip().split(',')
        for move in moves:
            x, y = move.split(':')
            distance += int(x)
            depth += int(y)
            fuel -= abs(int(x)) * LPM
            if not fuel or depth > MAX_DEPTH or depth < MIN_DEPTH:
                break
      
          
    #TRUCO: moves = [[int(h) for h in v.split(':')] for v in f.readline().strip().split(',')]

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')