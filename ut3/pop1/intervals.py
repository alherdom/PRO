# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    irange = []
    interval = "".join(interval)
    
    max_range = max(interval)
    print(max_range)
    
    
    if "[" in interval:
        min = int(interval[1])
    if "(" in interval:
        min = int(interval[1]) + 1
    if "]" in interval:
        max = 11
    if ")" in interval:
        max = 10
    for i in range(min, max):
        irange.append(i)
    return irange


if __name__ == '__main__':
    run('[3,10]')
