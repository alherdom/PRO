objetiv_x = 7
objetiv_y = 8
position_x = 0
position_y = 0

while position_x < objetiv_x and position_y < objetiv_y:
    print(f"({position_x}, {position_y})", end=" ")
    position_x += 1
    position_y += 2
    print(f"({position_x}, {position_y})", end=" ")
    position_x += 2
    position_y += 1
