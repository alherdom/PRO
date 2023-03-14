# Si utilizamos el operador * delante del nombre de un parámetro posicional, estaremos indicando que
# los argumentos pasados a la función se empaqueten en una tupla. Un ejemplo en el que vamos a implementar
# una función para sumar un número variable de valores. La función que tenemos disponible en Python no cubre este caso.

def _sum(*values):
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result


print(_sum(4, 3, 2, 1))