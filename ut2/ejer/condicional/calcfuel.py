# En esta kata tendrás que escribir una función que tome litros y precio_por_litro (en dólares) como argumentos.
# Las compras de 2 o más litros tienen un descuento de 5 céntimos por litro, las compras de 4 o más litros tienen un descuento
# de 10 céntimos por litro, y así cada dos litros, hasta un descuento máximo de 25 céntimos por litro. Pero el total
# descuento por litro no puede ser superior a 25 céntimos. Devuelve el coste total redondeado a 2 decimales. También se puede
# suponer que no habrá entradas negativas o no numéricas.


litros = float(input("INTRODUZCA LOS LITROS A REPOSTAR: "))
precio = float(input("INTRODUZCA EL PRECIO DE LA GASOLINA BASE: "))

if 2 <= litros < 4:
    descuento = 0.05 * litros
    precio_total = round(litros * precio - descuento, 2)
    print(precio_total)
elif 4 <= litros < 6:
    descuento = 0.10 * litros
    precio_total = round(litros * precio - descuento, 2)
    print(precio_total)
elif 6 <= litros < 8:
    descuento = 0.15 * litros
    precio_total = round(litros * precio - descuento, 2)
    print(precio_total)
elif 8 <= litros < 10:
    descuento = 0.20 * litros
    precio_total = round(litros * precio - descuento, 2)
    print(precio_total)
elif litros >= 10:
    descuento = 0.25 * litros
    precio_total = round(litros * precio - descuento, 2)
    print(precio_total)