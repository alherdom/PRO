# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
    max_points = 4
    games_player1 = games_player2 = 0
    points_player1 = points_player2 = 0
    for char in points:
        if char == "A":
            points_player1 += 1
        elif char == "B":
            points_player2 += 1
        if (points_player1 - points_player2) >= 2 and points_player1 >= max_points:
            games_player1 += 1
            points_player1 = points_player2 = 0
        elif (points_player2 - points_player1) >= 2 and points_player2 >= max_points:
            games_player2 += 1
            points_player1 = points_player2 = 0
        #TIE-BREAK!!
        if games_player1 == 6 and games_player2 == 6:
            max_points = 7
             

   
   
   
    return games_player1, games_player2


if __name__ == '__main__':
    run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')
