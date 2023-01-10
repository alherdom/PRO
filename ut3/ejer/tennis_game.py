# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    count_A = count_B = 0
    winner = "B"
    for char in points:
        if char == "A":
            count_A += 1
        elif char == "B":
            count_B += 1
    print("El jugador A tiene estos puntos",count_A)
    print("El jugador B tiene estos puntos",count_B)
    if (count_A - count_B) >= 2 and count_A >=4:
        games_A +=1
        count_A = 0
        
        winner = "A"
    return winner


if __name__ == '__main__':
    run('ABAABA')
