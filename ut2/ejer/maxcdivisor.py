# Escriba un programa que calcule el máximo común divisor entre dos números enteros.
# No utilice ningún algoritmo existente. Hágalo probando divisores.
# Entrada: a=12; b=44
# Salida: 4

a = 12
b = 44

if a < b:
    min = a
else:
    min = b

for i in range(min, 1, -1):
    if (a % i) and (b % i) == 0:
        print(i)
