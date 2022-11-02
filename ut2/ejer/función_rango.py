# Escriba un programa que calcule el valor de x para el que la función f(x)=x^2−6x+3 obtenga su menor resultado.
# Centre la búsqueda en el rango [−9,9] sólo con valores enteros.
# El resultado es: x=3 y f(x)=−6

x = 0
f = x**2 - 6 * x + 3

for num in range(-9, 9):
    x = num
    f = x**2 - 6 * x + 3
    print(f)
