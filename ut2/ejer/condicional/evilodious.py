# El número n es Maligno si tiene un número par de 1's en su representación binaria.
# Los primeros números Malignos: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20.
# El número n es Odioso si tiene un número impar de 1's en su representación binaria.
# Los primeros números Odiosos: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19.
# Tienes que escribir una función que determine si un número es Malvado o Odioso, la
# función debe devolver "¡Es Malvado!" en caso de número malvado y "¡Es Odioso!" en caso de número odioso.
int_cod = int(input("INTRODUZCA EL ENTERO PARA PASAR A BINARIO Y COMPROBAR: "))
bin_cod = bin(int_cod)
print(bin_cod)
count_1 = bin_cod.count('1')
if count_1 % 2 == 0:
    print("ES UN NUMERO MALVADO!")
else:
    print("ES UN NÚMERO ODIOSO!")