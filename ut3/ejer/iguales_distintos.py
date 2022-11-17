# Escriba un programa en Python que acepte una lista de valores numéricos y devuelva Iguales si todos los valores son iguales o Distintos en otro caso.
# Entrada: [1, 1, 1, 1, 1, 1, 1]
# Salida: Iguales

values = [1, 1, 1, 1, 1, 1, 1]
first_value = values[0]
output = []
for value in values:
    if value == first_value:
        first_value = value
        output.append(first_value)
    else:
        print("ALGUNO DE LOS VALORES DE LA LISTA SON DISTINTOS")
        print(values)
if values == output:
    print("TODOS LOS VALORES DE LA LISTA SON IGUALES")
    print(output)
# prueba