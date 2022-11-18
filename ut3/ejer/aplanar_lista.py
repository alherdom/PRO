# Escriba un programa en Python que acepte una lista – que puede contener sublistas (sólo en 1 nivel de anidamiento) – y genere otra lista «aplanada».
# Entrada: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Salida: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

entry = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened = []
for element in entry:
    if type(element) == list:
        flattened.extend(element) # AQUÍ DETECTO SI ESE ELEMENTO ES UNA LISTA (LISTA DENTRO DE OTRA LISTA) Y CON LA FUNCIÓN "extend()" EXTIENDO ESA SUBLISTA.
    else:
        flattened.append(element) # DESCARTO QUE EL ELEMENTO SEA SUBLISTA, Y AÑADO EL ELEMENTO NORMAL.
print(flattened)

