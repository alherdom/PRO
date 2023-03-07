# *******************
# NÚMERO EN INTERVALO
# *******************


def in_range(value: int, lower_limit: int, upper_limit: int) -> bool:
    interval = []
    for i in range(lower_limit, upper_limit+1):
        interval.append(i)
    if value in interval:
        return True
    return False
        
