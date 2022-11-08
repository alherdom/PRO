# Dado su tamaño, muestre por pantalla un mosaico donde la diagonal principal esté representada
#  por X, la parte inferior por D y la parte superior por U.
size = 5
for row in range(size):
    for col in range(size):
        if row > col:
            char = "U"
        elif col > row:
            char = "D"
        else:
            char = "X"
        print(char, end=" ")
    print()
