import re
# Escriba un programa en Python que indique si un determinado número es o no 
# un flotante válido en Python.

numbers = ('02.00', '02', '30.00.00', '3e0000', '3.0000_0000', '4.')
regex = r'\d+\.?e?\d+_?\d+?'
for number in numbers:
    output = re.match(regex, number)
    print(output)