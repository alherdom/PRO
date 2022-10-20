# Dada una cadena de texto, indique el número de vocales que tiene.
# Ejemplo.
# Entrada: Supercalifragilisticoespialidoso
# Salida: 15
word = "Supercalifragilisticoespialidoso"
vowels_count = 0
for letter in word:
    if letter == "a":
        vowels_count += 1
    if letter == "e":
        vowels_count += 1
    if letter == "i":
        vowels_count += 1
    if letter == "o":
        vowels_count += 1
    if letter == "u":
        vowels_count += 1
print(vowels_count)
