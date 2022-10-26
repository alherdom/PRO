# Dado su tamaño, muestre por pantalla un mosaico donde la diagonal principal esté representada
#  por X, la parte inferior por D y la parte superior por U.

for i in range(5):
    for j in range(5):
        if i > j:
            symbol = "U"
            print("U", end=" ")
        if i == j:
            print("X")
        if i < j:
            print("D", end=" ")
