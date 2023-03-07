# *******************
# NÚMERO EN INTERVALO
# *******************


def in_range(value: int, lower_limit: int, upper_limit: int) -> bool:
    interval = [i for i in range(lower_limit, upper_limit+1)]
    if value in interval:
        return True
    return False
        
