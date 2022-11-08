# Escriba un programa que muestre por pantalla todas las fichas del dominó. La ficha «en blanco» se puede representar con un 0.

DOMINO_MAX = 6
for blue in range(DOMINO_MAX + 1):
    for red in range(blue, DOMINO_MAX + 1):
        print(f"{blue}|{red}", end="")
    print()
