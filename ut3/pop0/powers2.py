'''
Dado un número entero no negativo obtenga una lista con todas las potencias de 2
con el exponente variando desde 0 hasta dicho valor (inclusive).

¿Podrías resolverlo también con listas por comprensión?
'''


def run(num_powers: int) -> list:
    powers2 = [2**i for i in range(num_powers + 1)]
    return powers2


if __name__ == '__main__':
    run(0)
