# Existe la posibilidad de usar el asterisco * en la llamada a la función para 
# desempaquetar los argumentos posicionales:

def _sum(*values):
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result

values = (4, 3, 2, 1)
print(_sum(*values))  # Desempaquetado
