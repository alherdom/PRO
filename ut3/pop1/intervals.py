# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    irange = []
    min = 3
    max = 10
    if interval.startswith('[') and interval.endswith("]"):
        min = 3
        max = 11
    if interval.startswith('(') and interval.endswith(")"):
        min = 4
        max = 10
    if interval.startswith('[') and interval.endswith(")"):
        min = 3
        max = 10
    if interval.startswith('(') and interval.endswith("]"):
        min = 4
        max = 11
 
    for i in range(min, max):
        irange.append(i)
    return irange


if __name__ == '__main__':
    run('[3,10]')
