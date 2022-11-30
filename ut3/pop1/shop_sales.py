# *******************************
# VENTAS EN TIENDA DE INFORM�TICA
# *******************************


def run(sales: list) -> tuple:
    flattened = []
    for element in sales:
        flattened.extend(element)
    pcs = sum(flattened[::2])
    displays = sum(flattened[1::2])
    return pcs, displays


if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])
