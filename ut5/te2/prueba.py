from itertools import combinations

cartas = ['🃖','🃗','🃋','🃍','🂹','🂢','🂣']
combinaciones = list(combinations(cartas, 5))
for combinacion in combinaciones:
    print(combinacion)
print(len(combinaciones))

# suits = []
# values = []

# for suit in suits:
#     if suits.count(suit) == 5:
#         return True

# # cuarteto poker 
# for value in values:
#     if values.count(value) == 4:
#         return True

# # trio
# for value in set(values):
#     if values.count(value) == 3:
#         return True
    
# # pareja
# for value in set(values):
#     if values.count(value) == 2:
#         return True