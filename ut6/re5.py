import re
# Escriba un programa en Python que obtenga el resultado de una operación 
# entre números enteros positivos. Las operación puede ser suma, resta,
# multiplicación o división, y puede haber espacios (o no) entre los operandos
# y el operador.
operations = ('4  +2', '3-  2','4 * 2','7/2' )
regexp = r'(\d)\s*?([+\-*\/])\s*?(\d)'
for operation in operations:
    m = re.search(regexp, operation)
    first_num = int(m[1])
    operator = m[2]
    second_num = int(m[3])
    match operator:
        case '+':
            print(first_num + second_num)
        case '-':
            print(first_num - second_num)
        case '*':
            print(first_num * second_num)
        case '/':
            print(first_num / second_num)