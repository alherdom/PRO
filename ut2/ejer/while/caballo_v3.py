objetiv_x = 7
objetiv_y = 8
position_x = 0
position_y = 0
movement = True  # Usamos este booleano para cambiar la alternancia entre los dos tipos de movimientos (x + 1, y + 2) y (x + 2, y + 1).
while position_x <= objetiv_x and position_y <= objetiv_y:
    print(f"({position_x}, {position_y})", end=" ")
    position_x += 2 - movement
    position_y += 1 + movement
    movement = not movement
print()
