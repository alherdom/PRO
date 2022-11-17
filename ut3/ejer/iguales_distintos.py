# Escriba un programa en Python que acepte una lista de valores numéricos y devuelva Iguales si todos los valores son iguales o Distintos en otro caso.
# Entrada: [1, 1, 1, 1, 1, 1, 1]
# Salida: Iguales

values = [1, 1, 2, 1, 1, 1, 1]

for value in values:
    if value == values[1]:
        print(f'{value} es igual a {values[1]}')
    