"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    target = 0
    prev = 0
    for number in values:
        if number != prev:
            prev = number + 1
            target = number
        else:
            target = None
    return target


"""
elements = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
prev = None
non_consecutive = []
for element in elements:
if element != prev:
prev = element
non_consecutive.append(element)
print(non_consecutive)
"""

if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
