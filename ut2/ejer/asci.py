# Escriba un programa que muestre (por filas) la Tabla ASCII, empezando con el código 33 y terminando con el 127.
min = 33
max = 127
for int in range(min, max):
    print(f"{int:03d} {chr(int)} ", end="")
    if (min + int) % 5 == 0:
        print()
