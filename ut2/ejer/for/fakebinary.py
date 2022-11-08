# Dada una cadena de dígitos, debe sustituir cualquier dígito inferior a 5 por '0'
# y cualquier dígito de 5 en adelante por '1'. Devuelve la cadena resultante.
str_digit = input("TECLEE UNA CADENA DE DÍGITOS: ")
result = ""
for digit in str_digit:
    if int(digit) < 5:
        result += "0"
    else:
        result += "1"
print(result)