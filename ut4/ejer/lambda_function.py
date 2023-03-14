# Funciones anónimas «lambda».
# Una función lambda tiene las siguientes propiedades:
# - Se escribe en una única sentencia (línea).
# - No tiene nombre (anónima).
# - Su cuerpo conlleva un return implícito.
#  - Puede recibir cualquier número de parámetros.
# Ejemplo de función «lambda» que nos permite contar el número de palabras de una cadena de texto:

num_words = lambda t: len(t.split())

# type(num_words)
# function

# num_words
# <function __main__.<lambda>(t)>

print(num_words('hola socio vamos a ver'))

# Otro ejemplo en el que mostramos una tabla con el resultado de aplicar el «and» lógico
# mediante una función «lambda» que ahora recibe dos parámetros:

logic_and = lambda x, y: x & y

for i in range(2):
    for j in range(2):
        print(f'{i} & {j} = {logic_and(i, j)}')