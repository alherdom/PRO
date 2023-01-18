# ***************************
# DICCIONARIO EN CONSTRUCCIÓN
# ***************************


def run(items: list) -> dict:
    unpack_items = {}
    flattened = []
    for item in items:
        if type(item) == list:
            flattened.extend(item)
        else:
            flattened.append(item)
    unpack_items = {flattened[0]:list(flattened)}
    
    print(flattened)
    return unpack_items


if __name__ == '__main__':
    run([['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]])
