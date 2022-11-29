'''
Dada una lista de entrada, devuelva True si todos sus elementos son iguales o
False en otro caso.
'''


def run(items: list) -> bool:
    all_same = True
    comparative_item = items[0]
    for item in items[1:]:
        if item != comparative_item:
            all_same = False           
            
    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
