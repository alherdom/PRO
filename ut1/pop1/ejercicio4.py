# ut1-pop1-ej4
hexcolor = 'A131F7'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
r = hexcolor[0:2]
g = hexcolor[2:4]
b = hexcolor[4:6]
r_decimal = int(r, 16)
g_decimal = int(g, 16)
b_decimal = int(b, 16)
rgb_color = f'({r_decimal},{g_decimal},{b_decimal})'
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert rgb_color == '(161,49,247)'