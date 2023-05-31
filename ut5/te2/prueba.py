from itertools import combinations

numeros = [1, 2, 3, 4, 5, 6, 7]
combinaciones = combinations(numeros, 5)
lista_combinaciones = list(combinaciones)

print(lista_combinaciones)
print(len(lista_combinaciones))