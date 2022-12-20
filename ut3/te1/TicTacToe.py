

import random

# ---------- Input welcome to start the game and assign each symbol -----------
print("\n❌⭕ WELCOME TO TICTACTOE GAME ⭕❌\n")
print("RULES: 📋\n🔹 The game is played on a grid that's 3 squares by 3 squares.\n🔹 One player plays with X and the other with O, by random assignment.\n🔹 There is no universally-agreed rule as to who plays first, but in this 'pygame' X plays first. \n🔹 Players take turns putting their marks ONLY in empty squares, else lose the turn.\n🔹 The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n🔹 When all 9 squares are full, the game is over.\n")

player1_name = input("👾 Player1 enter your name: ")
player2_name = input("👽 Player2 enter your name: ")
player1 = random.randint(0, 1)

if player1:
    print(f"\n{player1_name}, you will play with crosses ❌")
    print(f"{player2_name}, you will play with noughts ⭕\n")
    crosses_player = player1_name
else:
    print(f"\n{player1_name}, you will play with noughts ⭕")
    print(f"{player2_name}, you will play with crosses ❌\n")
    crosses_player = player2_name

# ------------------------- Create and print the grid -------------------------
GRID_SQUARES = ["0️⃣ ", "1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ "]
SQUARE_SIZE = len(GRID_SQUARES) ** 0.5
i = 0
row = []
grid = []

for square in GRID_SQUARES:
    row.append(square)
    i += 1
    if i % SQUARE_SIZE == 0:
        row = " | ".join(row)
        grid.append(row)
        row = []
grid = "\n—————————————\n".join(grid)
print(grid)
print(f"\nCrosses(❌) start so {crosses_player} you first ⚡")

# ------------------------------------ GAME -----------------------------------
turn = True
crosses = []
noughts = []
have_a_winner = False
grid = []
WINNING_SQUARES = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[2, 5, 8],[1, 4, 7],[6, 7, 8],[3, 4, 5],[2, 4, 6]]

for _ in GRID_SQUARES:
    if have_a_winner:
        break
    selected_square = int(input("\nEnter a number[0-8]: "))
    while selected_square >= len(GRID_SQUARES) or selected_square < 0:
        selected_square = int(input("💢 Grrrr!!!😾 Enter a number between 0 and 8! Try again 😻:\n"))
    if GRID_SQUARES[(selected_square)] == "❌" or GRID_SQUARES[(selected_square)] == "⭕":
        selected_square = "💩"
        print("⛔ Error: You're trying to mark in a filled square!🚷 Sorry, but you lose your turn!🔄\n")
    if turn:
        symbol = "❌"
        turn = False
        crosses.append(selected_square)
    else:
        symbol = "⭕"
        turn = True
        noughts.append(selected_square)
    if selected_square != "💩":
        GRID_SQUARES[(selected_square)] = symbol

    # ------------------------ Check out the winner -------------------------
    crosses_in_row, noughts_in_row = 0, 0
    for win_combi in WINNING_SQUARES:
        crosses_in_row, noughts_in_row = 0, 0
        for num in win_combi:
            if num in crosses:
                crosses_in_row += 1
            if num in noughts:
                noughts_in_row += 1
        if crosses_in_row == SQUARE_SIZE or noughts_in_row == SQUARE_SIZE:
            have_a_winner = True
            break

    # ---------------------------- Print the grid -----------------------------
    i = 0
    for square in GRID_SQUARES:
        row.append(square)
        i += 1
        if i % SQUARE_SIZE == 0:
            row = " | ".join(row)
            grid.append(row)
            row = []
    grid = "\n—————————————\n".join(grid)
    print()
    print(grid)
    grid = []
# ----------------------------- Who win the game ------------------------------
if have_a_winner:
    print(f"\n{symbol} ¡WIN! 🏆 Well done. 🏆")
else:
    print("\nNo one wins! 😿")
# -----------------------------------------------------------------------------
"""---------------------- TicTacToe2.0 n x n in progres...----------------------
import sys
n = int(sys.argv[1])
values = [i for i in range(n * n)]
grid_squares = [(values[i : i + n]) for i in range(len(values) - n + 1) if i % n == 0]
values = [(grid_squares[j][i]) for i in range(0, n) for j in range(0, n)]
for i in range(0, n):
    values.append(i * (n + 1))
for i in range(0, n):
    values.append((i + 1) * (n - 1))
winning_combinations = [values[i : i + n] for i in range(len(values) - n + 1) if i % n == 0]
"""