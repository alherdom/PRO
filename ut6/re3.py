import re
# Escriba un programa en Python que indique si un determinado número es o no 
# un flotante válido en Python.
numbers = ('4.0', '4.', '04.0', '04.', '4.000_000', '4e0', '40', '1,000', '4000_000.0', '4000_000')
regex = r'(\b\d+\.\d*\_*\d*)|(\de0\b)'
for number in numbers:
    output = re.match(regex, number)
    print(output)

text = 'Esto si es un número flotante: 4.0, y esto: 4., y esto también: 04.0, y esto también lo es: 04., y esto: 4.000_000, y esto: 4e0, pero esto no es un flotante: 40, ni tampoco esto: 1,000, pero esto si: 4000_000.0, esto no: 4000_000'
floats = re.findall(regex, text, re.I)
print(floats)