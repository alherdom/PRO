# In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount
# of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total
# discount per litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places. Also you can
# guess that there will not be negative or non-numeric inputs.

litros = int(input("INTRODUZCA LOS LITROS A REPOSTAR: "))
precio = float(input("INTRODUZCA EL PRECIO DE LA GASOLINA BASE: "))

if 2 < litros < 4:
    descuento = 1 - (0.05 * litros)
    precio_total = litros * precio * descuento
    print(precio_total)