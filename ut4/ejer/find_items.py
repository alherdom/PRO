def find_items(items,value):
    '''
    Cuenta el numero de veces que aparece "valor" dentro de
    "items".

    :param items: tupla con todos los valor
    :type items: tuple
    :param valor: valor a comprobar sus repeticiones
    :type valor: int

    :return: numero de repeticiones
    :rtype: int
    '''
    count = len([i for i in items if i == value])
    return count

input = (1,2,2,2,1,3,2,4)
target = 2
print(find_items(input,target))

