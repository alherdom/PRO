# ***************
# TUPLA DE DUPLAS
# ***************


def run(input: tuple) -> set:
    for item in input:
        value1 = item[0][0]
        value2 = item[0][1]
        print(value1, value2)
    output = set(input)
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))

