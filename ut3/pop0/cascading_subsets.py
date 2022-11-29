# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    cascading = []
    if size == 3:
        cascading.append(values[:size])
        cascading.append(values[1:])
    elif size == 2:
        cascading.append(values[:size])
        cascading.append(values[1:size+1])
        cascading.append(values[size:])
    elif size == 1:
        i = 0
        for value in values:
            cascading.append(values[i:i+1])
            i += 1
    
    return cascading


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)
