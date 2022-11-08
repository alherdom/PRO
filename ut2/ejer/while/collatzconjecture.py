# Programa que imprima todos los "pasos" de la conjetura de COLLATZ
# hasta llegar al 1.
number = int(input("TECLEE EL NÚMERO PARA COLLATZ: "))
while number != 1:
    if number % 2 == 0:
        number = number / 2
        print(number)
    else:
        number = number + 1
        print(number)
        
    