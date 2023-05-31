from itertools import combinations

cartas = ['🃖','🃗','🃋','🃍','🂹','🂢','🂣']
combinaciones = list(combinations(cartas, 5))
for combinacion in combinaciones:
    print(combinacion)
print(len(combinaciones))