#Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando
#(suma, resta, multiplicación, división) y calcule el resultado de la operación, usando para
#ello la sentencia match-case. Controlar que la operación no sea una de las cuatro predefinidas.
#En este caso dar un mensaje de error y no mostrar resultado final.
# Ejemplo
#     Entrada: 4, 3, +
#     Salida: 4+3=7
number_1 = int(input('Teclee el primer número: '))
number_2 = int(input('Teclee el segundo número: '))
oper = input('Teclee la operación deseada [+,-,*,/]: ')
match oper:
    case '+':
        result = number_1 + number_2
    case '-':
        result = number_1 - number_2
    case '*':
        result = number_1 * number_2
    case '/':
        result = number_1 / number_2
    case _:
        result = None
        print('OPERANDO INCORRECTO, ESCOJA UNA DE LOS SIGUIENTE(+,-,*,/)')
if result is None:
    print('Algo va mal')
else:
    print(f'{number_1}{oper}{number_2}={result}')