# Escriba un programa que permita al usuario adivinar un número. Indicar si el número buscado
# es menor o mayor que el que se está preguntando y mostrar igualmente el número de intentos
# hasta encontrar el número objetivo
TARGET_NUMBER = int(input("ESTABLEZCA EL NÚMERO A ADIVINAR: "))
number = None
num_tries = 0
while number != TARGET_NUMBER:
    number = int(input("TECLEE UN NÚMERO: "))
    num_tries += 1
    if number > TARGET_NUMBER:
        print("EL NÚMERO TIENE QUE SER MENOR")
    elif number < TARGET_NUMBER:
        print("EL NÚMERO TIENE QUE SER MAYOR")
print(f"✅ ¡ENHORABUENA! HAS ENCONTRADO EL NÚMERO EN {num_tries} INTENTOS")
