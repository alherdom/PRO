# Escriba un programa en Python que acepte dos valores enteros (𝑥 e 𝑦) que representarán
# un punto (objetivo) en el plano. El programa simulará el movimiento de un «caballo»
# de ajedrez moviéndose de forma alterna: 2 posiciones en 𝑥 + 1 posición en 𝑦. El siguiente
# movimiento que toque sería para moverse 1 posición en 𝑥 + 2 posiciones en 𝑦. El programa
# deberá ir mostrando los puntos por los que va pasando el «caballo» hasta llegar al punto objetivo.
# Entrada: objetivo_x=7; objetivo_y=8;
# Salida: (0, 0) (1, 2) (3, 3) (4, 5) (6, 6) (7, 8)

objetiv_x = 7
objetiv_y = 8
position_x = 0
position_y = 0
print(f'({position_x}, {position_y})', end=' ')
movement = True # Usamso este booleano para cambiar la alternancia entre los dos tipos de movimientos (x + 1, y + 2) y (x + 2, y + 1).
while position_x != objetiv_x and position_y != objetiv_y:
    if movement:
        position_x += 1
        position_y += 2
    else:
        position_x += 2
        position_y += 1
    print(f'({position_x}, {position_y})', end=' ')
    movement = not movement

