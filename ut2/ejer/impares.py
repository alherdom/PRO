numero = int(input("TECLEE UN NÚMERO ENTERO POSITIVO: "))
for i in range (0, numero + 1):
    if i % 2 != 0:
        print(i,end=",")
    