import re
# Escriba un programa en Python que indique si un determinado número es o no 
# un flotante válido en Python.

number1 = '02.00' 
number2 = '02'
number3 = '30.00.00'

regex = r'\d+\.\d+'
output = re.match(regex, number2)
print(output)