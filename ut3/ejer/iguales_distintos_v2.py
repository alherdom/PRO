# Escriba un programa en Python que acepte una lista de valores numéricos y devuelva Iguales si todos los valores son iguales o Distintos en otro caso.
# Entrada: [1, 1, 1, 1, 1, 1, 1]
# Salida: Iguales

values = [1, 1, 1, 1, 1, 1, 1]
first_value = values[0]
for value in values[1:]:
    if value != first_value:
        print("Distintos")
        break
else:
    print("Iguales")

# version 2
# first_value = values[0]
# if values.count(first_values) != len(value):
