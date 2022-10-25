# Determine si un número dado es un número primo.
# No es necesario implementar ningún algoritmo en concreto. La idea es probar los números menores al dado e ir viendo si las divisiones tienen resto cero o no.
# ¿Podría optimizar su código? ¿Realmente es necesario probar con tantos divisores?
# Ejemplo
# Entrada: 11
# Salida: Es primo

number = 11
num_divisors = 2
poss_div = 0

for poss_div in range(1, number + 1):
    if number % poss_div == 0:
        num_divisors += 1
print(num_divisors)
