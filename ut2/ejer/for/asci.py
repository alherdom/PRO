# Escriba un programa que muestre (por filas) la Tabla ASCII, empezando con el código 33 y terminando con el 127.
cod1 = 33
cod2 = 127
for int in range(cod1, cod2 + 1): 
    print(f"{int:03d} {chr(int)} ", end="")
    if (cod1 + int) % 5 == 0:
        print()
