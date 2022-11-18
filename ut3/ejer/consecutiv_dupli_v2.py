# Escriba un programa en Python que acepte una lista y genere otra lista eliminando los elementos duplicados consecutivos.
# Entrada: [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

elements = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
no_dupli_element = None
output = []
for element in elements:
    if element != no_dupli_element:
        no_dupli_element = element
        output.append(element)
print(output)
