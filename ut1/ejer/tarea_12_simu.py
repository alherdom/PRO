# ut1-pop0-ej1
seconds = 31256
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
hours = seconds // 3600
seconds_rest = seconds % 3600
minutes = seconds_rest // 60
seconds = seconds % 60
print(hours)
print(minutes)
print(seconds)
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert hours == 8
assert minutes == 40 
assert seconds == 56