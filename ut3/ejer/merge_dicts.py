# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    merged = {}
    merge = {**d1,**d2}
    return merged


if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})

