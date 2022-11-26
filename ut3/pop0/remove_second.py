'''
Dada una lista, genere otra lista eliminando el segundo elemento de forma repetida.
'''


def run(items: list) -> list:
    filter = items[::2]
    return filter
