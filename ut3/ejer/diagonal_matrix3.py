# Escriba un programa en Python que acepte una lista de listas representando una matriz numérica y compute la suma de los elementos de la diagonal principal.
# Entrada: [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
# Salida: 20
# matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
# diagonal = matrix[0][0] + matrix[1][1] + matrix[2][2]
# print(diagonal)

matrix = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]

main_diagonal = [matrix[i][i] for i in range(len(matrix))]
sum_diagonal = sum(main_diagonal)
print(sum_diagonal)
