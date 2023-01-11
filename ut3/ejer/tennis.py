points = 'BBBBAAAABBBBBBBBAAAAAAAAAAAABBBBBBBBBBBBAAAAAAAAAAAA'
points_a = points_b = 0
games_a = games_b = 0
winner = ""
for char in points:
    if char == "A":
        points_a += 1
    elif char == "B":
        points_b += 1
    if abs(points_a - points_b) >= 2 and points_a >=4:
        games_a += 1
        points_a = points_b = 0
    elif abs(points_a - points_b) >= 2 and points_b >=4:
        games_b += 1
        points_a = points_b = 0
if (games_a == 6 and abs(games_a - games_b) >= 2) or (games_b == 6 and games_a == 7):
    winner = "A"
elif (games_b == 6 and abs(games_a - games_b) >= 2) or (games_a == 6 and games_b == 7):
        winner = "B"
print("Los puntos del Jugador A son:",games_a)
print("Los puntos del Jugador B son:",games_b)
print("Gana el partido el Jugador:",winner)
if winner == "":
    print("No hay ganador")

   
