import random

COORDINATES = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C"]
turns = ["⭕", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"]
i = 0
row = []
TOTAL_COORDINATES = len(turns)

player1_name = input("Welcome to TicTacToe game. Player1 type your name: ")
player2_name = input("Player2 type your name: ")

player1 = random.randint(0, 1)

if player1:
    player2 = 0
    print(f"\n{player1_name}, you will play with crosses ❌")
    print(f"{player2_name}, you will play with noughts ⭕\n")
    for coordinate in range(TOTAL_COORDINATES):
        row.append(COORDINATES[coordinate])
        i += 1
        if i % 3 == 0:
            row = " | ".join(row)
            print(row)
            row = []
            print("-------------")
    print()
    coordinate_player1 = input(
        f"Crosses start so {player2_name} you first, type the coordinate: "
    )
else:
    player2 = 1
    print(f"\n{player1_name}, you will play with noughts ⭕")
    print(f"{player2_name}, you will play with crosses ❌\n")
    for coordinate in range(TOTAL_COORDINATES):
        row.append(COORDINATES[coordinate])
        i += 1
        if i % 3 == 0:
            row = " | ".join(row)
            print(row)
            row = []
            print("-------------")
    print()
    coordinate_player2 = input(
        f"Crosses start so {player2_name} you first, type the coordinate: "
    )

i = 0
row = []

for coordinate in range(TOTAL_COORDINATES):
    row.append(turns[coordinate])
    i += 1
    if i % 3 == 0:
        row = " | ".join(row)
        print(row)
        row = []
        print("-------------")
