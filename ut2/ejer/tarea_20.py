# Escriba un programa que encuentre todos los múltiplos de 5 menores que un valor dado:
# Ejemplo
# Entrada: 36
# Salida: 5 10 15 20 25 30 35
num_limit = 36
mult5 = 0
while mult5 < num_limit:
    mult5 += 1
    if mult5 % 5 == 0:
        print("Este número si es múltiplo", mult5)
