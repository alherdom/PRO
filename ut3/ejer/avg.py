# Lea desde línea de comandos una serie de números y obtenga la media de dichos valores (muestre el resultado con 2 decimales).

# La llamada se haría de la siguiente manera: $ python3 avg.py 32 56 21 99 12 17

import sys

# En values tendremos una lista con los valores (como strings)
values = sys.argv[1:]
# values = [32, 56, 21, 99, 12, 17]
# Su código debajo de aquí
len_list = len(values)
media = sum(values) / len_list
print(media)
