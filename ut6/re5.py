import re
# Escriba un programa en Python que obtenga el resultado de una operación 
# entre números enteros positivos. Las operación puede ser suma, resta,
# multiplicación o división, y puede haber espacios (o no) entre los operandos
# y el operador.
operations = ('  5 *  1 ', '4  +2', '3-  2', '4 * 2', '7/2' )
regexp = r'(\d)\s*([+\-*/])\s*(\d)'
for operation in operations:
    m = re.search(regexp, operation)
    left_oper, operator, rigth_oper = m.groups()
    left_oper = int(left_oper)
    rigth_oper = int(rigth_oper)
    match operator:
        case '+':
            print(left_oper + rigth_oper)
        case '-':
            print(left_oper - rigth_oper)
        case '*':
            print(left_oper * rigth_oper)
        case '/':
            print(left_oper / rigth_oper)