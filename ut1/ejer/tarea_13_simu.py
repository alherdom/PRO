#Escribe un programa en Python que dada una secuencia de ADN calcule el porcentaje de presencia de cada base (sobre el total).
# ut1-pop0-ej2
adn = 'GGTTACCAACCCAGTCGAAGGTCATGAAGGGGCGTATTTGGATGGAGCTG'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
count_g = adn.count('G')
count_a = adn.count('A')
count_t = adn.count('T')
count_c = adn.count('C')
len_adn = len(adn)
adenines_rate = (count_a / len_adn) * 100
thymines_rate = (count_t / len_adn) * 100
guanines_rate = (count_g / len_adn) * 100
cytosines_rate = (count_c / len_adn) * 100
print(adenines_rate, thymines_rate, guanines_rate, cytosines_rate)
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert adenines_rate == 24.0
assert thymines_rate == 22.0
assert guanines_rate == 36.0
assert cytosines_rate == 18.0