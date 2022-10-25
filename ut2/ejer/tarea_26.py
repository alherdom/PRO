# Escriba un programa en Python que acepte un número entero n y realice el siguiente cálculo de productos sucesivos.
n = 5
result = 1
for i in range(1, n + 1):
    result *= n**2
print(result)
