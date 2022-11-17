# Escriba un programa en Python que acepte una lista de valores numéricos y obtenga su valor máximo sin utilizar la función «built-in» max().
# Entrada: [6, 3, 9, 2, 10, 31, 15, 7]
# Salida: 31
# ERROR
values = [6, 3, 9, 2, 10, 31, 15, 7]
max_value = values[0]
for value in values[1:]:
    if value > max_value:
        max_value = value
print(value)
