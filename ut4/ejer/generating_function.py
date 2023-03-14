# Funciones generadoras.
# Se escriben como funciones ordinarias con el matiz de incorporar la sentencia yield que sustituye, 
# de alguna manera, a return. Esta sentencia devuelve el valor indicado y, a la vez, «congela» el estado
# de la función hasta la siguiente llamada.
# Ejemplo en el que escribimos una función generadora de números pares:

def evens(lim):
    for i in range(0, lim + 1, 2):
        yield i

# type(evens)
# function

evens_gen = evens(20)  # retorna un generador

# type(evens_gen)
# generator

# for even in evens_gen:
#     print(even, end=' ')
    
for even in evens(20):
    print(even, end=' ')
    
# Explicitar lista de valores:
list(evens(20))

# Detalle muy importante es que los generadores «se agotan». Es decir, una vez que ya hemos 
# consumido todos sus elementos, no obtendremos nuevos valores.
