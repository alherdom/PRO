# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path
MIN_DEPTH = 0
MAX_DEPTH = 600
CONSUMPTION_RATE = 3
def run(route_path: Path) -> tuple:
    distance = depth = 0
    with open(route_path) as f:
        fuel = int(f.readline())
        moves = [[int(h) for h in v.split(':')] for v in f.readline().strip().split(',')]
        for x, y in moves:
            distance += x
            depth += y
            fuel -= abs(x) * CONSUMPTION_RATE
            if not fuel or depth > MAX_DEPTH or depth < MIN_DEPTH:
                break
      
          
      

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')