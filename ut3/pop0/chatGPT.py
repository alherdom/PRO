# define the grid
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

# define the players
player1 = 'X'
player2 = 'O'

# define the current player
current_player = player1

# define a flag to check if the game is over
game_over = False

# define a function to print the grid
def print_grid():
  for row in grid:
    print(' '.join(row))

# define a function to check if a player has won the game
def check_win():
  # check rows
  for row in grid:
    if row[0] == row[1] == row[2] and row[0] != ' ':
      return row[0]
  # check columns
  for col in range(3):
    if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
      return grid[0][col]
  # check diagonals
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
    return grid[0][0]
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
    return grid[0][2]
  # check if the game is a draw
  if ' ' not in grid[0] and ' ' not in grid[1] and ' ' not in grid[2]:
    return 'draw'
  # if no winner or draw, return None
  return None

# define the main game loop
while not game_over:
  # print the grid
  print_grid()
  # ask the current player for their move
  move = input(f'{current_player}, where do you want to move? (row, col): ')
  # parse the move
  row, col = move.split(',')
  row = int(row)
  col = int(col)
  # check if the move is valid
  if grid[row][col] == ' ':
    # make the move
    grid[row][col] = current_player
    # check if the current player has won the game
    winner = check_win()
    if winner:
      # print the grid
      print_grid()
      # print the winner
      print(f'{winner} wins!')
      # set the game_over flag to True
      game_over = True
    else:
      # switch players
      if current_player == player1:
        current_player = player2
      else:
        current_player = player1
  else:
    # if the move is not valid, print an error message
    print('Invalid move!')
