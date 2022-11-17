# Escriba un programa en Python que acepte una lista de valores numéricos y obtenga su valor máximo sin utilizar la función «built-in» max() (solución).
# Entrada: [6, 3, 9, 2, 10, 31, 15, 7]
# Salida: 31
values = [6, 3, 9, 2, 10, 31, 15, 7]
new_values = sorted(values, reverse=True)
print(new_values[0])
