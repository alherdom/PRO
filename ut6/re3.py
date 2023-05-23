import re
# Escriba un programa en Python que indique si un determinado número es o no 
# un flotante válido en Python.

numbers = ('4.0', '4.', '04.0', '04.', '4.000_000', '4e0', '40', '1,000')
regex = r'(\d+\.)|(\de0\b)'
for number in numbers:
    output = re.match(regex, number)
    print(output)