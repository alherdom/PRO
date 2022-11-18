# Escriba un programa en Python que acepte una lista de valores numéricos y devuelva Iguales si todos los valores son iguales o Distintos en otro caso.
# Entrada: [1, 1, 1, 1, 1, 1, 1]
# Salida: Iguales

values = [1, 1, 1, 1, 1, 1, 2]
first_value = values[0]
output = []
different = False
for value in values:
    if value != first_value:
        different = True 
    else:
        different = False
if different:
    print("Distintos")
else:
    print("Iguales")