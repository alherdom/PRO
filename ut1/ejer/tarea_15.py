# Escriba un programa en Python que acepte 3 números y calcule el mínimo (solución).
# Entrada: 7, 4, 9
# Salida: 4
number1 = int(input('Teclee el primer número: '))
number2 = int(input('Teclee el segundo número: '))
number3 = int(input('Teclee el tercer número: '))
if number1 < number2:
    if number1 < number3:
        minimun_number = number1
    else:
        min_value = number3
elif number2 < number3:
    minimun_number = number2
else:
    minimun_number = number3 
print(minimun_number)
