# *******************************
# VENTAS EN TIENDA DE INFORM�TICA
# *******************************


def run(sales: list) -> tuple:
    pcs = displays = 0   
    for sale in sales:
        pcs += sale[0]
        displays += sale[1]
    return pcs, displays           
    '''flattened = []
    for element in sales:
        flattened.extend(element)
    pcs = sum(flattened[::2])
    displays = sum(flattened[1::2])'''
if __name__ == '__main__':
    run([[4, 5], [1, 3], [3, 2]])
