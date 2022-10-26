# Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud.
# Entrada: 0001010011101 y 0000110010001
# Salida: 4
cod1 = "0001010011101"
cod2 = "0000110010001"
position1 = 0
position2 = 0

same_char = True

while same_char == True:
    position1 += 1
    position2 += 1
    same_char = cod1[position1] in cod2[position2]
    print(f'({cod1[position1]}, {cod2[position2]})', same_char, end=' ')  
else:
    print(f'({cod1[position1]}, {cod2[position2]})', same_char, end=' ')  
    # same_char = not same_char

