"""
El objetivo es encontrar el primer número no consecutivo dentro de una lista de valores
numéricos enteros. Si todos los valores son consecutivos entonces el resultado es None.
"""


def run(values: list) -> int:
    target = None    
    if len(values) > 1:
        first_value = values[0]
        for value in values[1:]:
            if value != first_value + 1:
                target = value
                break
            first_value += 1
    return target

 


if __name__ == "__main__":
    run([1, 2, 3, 4, 6, 7, 8])
