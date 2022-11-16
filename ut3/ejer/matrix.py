# Escriba un programa que permita multiplicar únicamente matrices de 2 filas por 2 columnas. Veamos un ejemplo concreto:
# A = [[6, 4], [8, 9]]
# B = [[3, 2], [1, 7]]
# El producto P=A×B se calcula siguiendo la multiplicación de matrices tal y como se indica a continuación:

A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

p00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
p01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
p10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
p11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

pmatrix = [[p00, p01], [p10, p11]]
print(f"{pmatrix[0]}\n{pmatrix[1]}")
