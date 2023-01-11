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
    if (count_A - count_B) >= 2 and count_A >=4:
        count_A = 0
        winner = "A"
    return winner


if __name__ == '__main__':
    run('ABAABA')
