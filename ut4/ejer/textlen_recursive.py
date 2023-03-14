# Otra aproximación a la recursividad se da en problemas donde tenemos que procesar 
# una secuencia de elementos. Supongamos que nos piden calcular la suma de las longitudes
# de una serie de palabras definidas en una lista:

def get_size(words: list[str]) -> int:
    if len(words) == 0:
        return 0
    return len(words[0]) + get_size(words[1:])

words = ['this', 'is', 'recursive']
print(get_size(words))