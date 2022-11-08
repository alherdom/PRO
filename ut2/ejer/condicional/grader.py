# Crea una función que tome un número como argumento y devuelva una
# calificación basada en ese número.
# Anything greater than 1 or less than 0.6	"F"
# 0.9 or greater	"A"
# 0.8 or greater	"B"
# 0.7 or greater	"C"
# 0.6 or greater	"D"
calificacion = float(input("TECLEE LA NOTA DEL ALUMNO: "))
if calificacion < 0.6:
    print("La CALIFICACION del alumno es F")
elif 0.6 <= calificacion < 0.7:
        print("La CALIFICACION del alumno es D")
elif 0.7 <= calificacion < 0.8:
        print("La CALIFICACION del alumno es C")
elif 0.8 <= calificacion < 0.9:
        print("La CALIFICACION del alumno es B")
elif 0.9 <= calificacion < 1:
        print("La CALIFICACION del alumno es A")
