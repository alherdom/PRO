# Escriba un programa en Python que realice las siguientes 9 multiplicaciones. ¿Nota algo raro?
one = "1"
num_mult = 10
for i in range(1, num_mult):
    factor = int(
        one * i
    )  # multiplico el string del numero ("1") por i, multplico la cadena
    result = factor * factor
    print(f"{factor} · {factor} = {result}")
