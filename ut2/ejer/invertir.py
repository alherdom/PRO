inversion = int(input("TECLEE LA CANTIDAD A INVERTIR: "))
interes = int(input("TECLEE EL TIPO DE INTERÉS: "))
años = int(input("TECLEE LA CANTIDAD DE AÑOS: "))

for i in range (1, años + 1):
    capital = inversion * ((1 + interes/100) ** i)
    print(f'EL AÑO {i} HA GANADO {int(capital)} €UROS')