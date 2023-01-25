# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    """set1 = set([value[0] for value in input])
       set2 = set([value[1] for value in input])""" 
    values1 = set()
    values2 = set()
    for first, second in input:
        values1.add(first)
        values2.add(second)
    output = (values1,values2)
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))