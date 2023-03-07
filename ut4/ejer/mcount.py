# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple, target: int) -> int:
    count = 0
    for item in items:
        if target == item:
            count+=1
    return count

