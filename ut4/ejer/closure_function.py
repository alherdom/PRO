# Una clausura (del término inglés «closure») establece el uso de una función interior 
# que se genera dinámicamente y recuerda los valores de los argumentos con los que fue creada:

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

m3 = make_multiplier_of(3)
m5 = make_multiplier_of(5)

# # type(m3)
# # function
# m3(7)  # 7 * 3

# # type(m5)
# # function
# m5(8)  # 8 * 5

# make_multiplier_of(5)(8)  # Llamada directa!

