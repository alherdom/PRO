# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    values1 = set()
    values2 = set()
    for items in input:
        values1.add(items[0])
        values2.add(items[1])
    output = (values1,values2)
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))