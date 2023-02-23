# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = []
    for item in unsorted_items.items():
         sorted_items.append(item)
    sorted_items = sorted(sorted_items, key=lambda t: t[1])
    return sorted_items
if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})