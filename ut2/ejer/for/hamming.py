# Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la misma longitud.
# Entrada: 0001010011101 y 0000110010001
# Salida: 4
cod1 = "0001010011101"
cod2 = "0000110010001"
hamming = 0

for i in range(len(cod1)):
    if cod1[i] != cod2[i]:
        hamming += 1
print(hamming)
