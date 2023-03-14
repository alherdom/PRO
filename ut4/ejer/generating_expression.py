# Una expresión generadora es sintácticamente muy similar a una lista por comprensión,
# pero utilizamos paréntesis en vez de corchetes. Se podría ver como una versión acortada 
# de una función generadora. Ejemplo en el que creamos números pares hasta el 20:

evens_gen = (i for i in range(0, 20, 2))

# type(evens_gen)
# generator

for i in evens_gen:
    print(i, end=' ')

# Una expresión generadora se puede explicitar, sumar, buscar su máximo o su mínimo,
# o lo que queramos, tal y como lo haríamos con un iterable cualquiera:

list(i for i in range(0, 20, 2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

sum(i for i in range(0, 20, 2))
# 90

min(i for i in range(0, 20, 2))
# 0

max(i for i in range(0, 20, 2))
# 18