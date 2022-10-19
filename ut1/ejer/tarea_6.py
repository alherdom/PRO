#Escriba un programa en Python que acepte un «string» con los 8 dígitos de un NIF, y calcule su dígito de control (solución).
#Entrada: 12345678 Salida: 12345678Z
letter_string = 'TRWAGMYFPDXBNJZSQVHLCKE'
dni_number = 12345678
rest = dni_number % 23
print(f'{dni_number}{letter_string[rest]}')