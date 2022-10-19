#Escriba un programa en Python que acepte un entero n y compute el valor de n + nn + nnn.
#Entrada: 5 Salida: 615 (5 + 55 + 555)
n = input('Teclea el número entero: ')
nn = n*2
nnn = n*3
print(int(n)+int(nn)+int(nnn),'(',n,'+',nn,'+',nnn,')')