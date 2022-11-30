# *******************************
# VENTAS EN TIENDA DE INFORM�TICA
# *******************************


def run(sales: list) -> tuple:
    pcs = 0
    displays = 0
    for element in sales:
        pcs += sales[0]
        displays += sales[1]
    '''flattened = []
    for element in sales:
        flattened.extend(element)
    pcs = sum(flattened[::2])
    displays = sum(flattened[1::2])
    return pcs, displays'''


if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])
