# Escriba un programa en Python que acepte una lista de valores numéricos y devuelva Iguales si todos los valores son iguales o Distintos en otro caso.
# Entrada: [1, 1, 1, 1, 1, 1, 1]
# Salida: Iguales

values = [1, 1, 1, 1, 1, 1, 1]
first_value = values[0]
output = []
if values.count(values[0]) == len(values):
    print("Iguales")
else:
    print("Distintos")
