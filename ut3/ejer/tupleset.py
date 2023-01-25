# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    values1 = []
    values2 = []
    output = set()
    for item in input:
        values1.append(item[0])
        values2.append(item[1])
    values1 = tuple(values1)
    values2 = tuple(values2)
    output = (set(values1),set(values2))
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))