# Escriba un programa que encuentre la mínima secuencia de múltiplos de 3 (distintos) cuya suma sea igual o superior a un valor dado.
# Ejemplo
# Entrada: 45
# Salida: 0, 3, 6, 9, 12, 15
suma = 0
while suma != 45:
    suma += 1
    print(suma)
    if suma % 3 == 0:
        print("Este número si es múltiplo", suma)
