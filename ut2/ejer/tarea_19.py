# Dada una cadena de texto, indique el número de vocales que tiene.
# Ejemplo.
# Entrada: Supercalifragilisticoespialidoso
# Salida: 15
WORD = "Supercalifragilisticoespialidoso"
vowels = "aeiu"
vowels_count = 0
if vowels in WORD:
    vowels_count += 1
print(vowels_count)

# for letter in WORD:
# if letter == "a":
# vowels_count += 1
# if letter == "e":
# vowels_count += 1
# if letter == "i":
# vowels_count += 1
# if letter == "o":
#     vowels_count += 1
# if letter == "u":
# vowels_count += 1
