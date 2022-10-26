# Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud.
# Entrada: 0001010011101 y 0000110010001
# Salida: 4
cod1 = "0001010011101"
cod2 = "0000110010001"
position1 = 0
position2 = 0
large1 = len(cod1)
large2 = len(cod2)

while large1 == large2:
    position1 += 1
    position2 += 1
    if cod1[position1] == cod2[position2]:
        print("Same")
    else:
        print("Not same")

