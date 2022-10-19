#Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es.
#Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100
#o bien si es divisible entre 400. Puedes hacer la comprobación en esta lista de años bisiestos.
#Entrada: 2008
#Salida: 
year = int(input("Teclee el año a comprobar: "))
module_4 = year % 4
module_100 = year % 100
module_400 = year % 400
if (module_4 == 0 and module_100 != 0) or module_400 == 0:
        print("Es un año bisiesto")
else:
    print("No es un año bisiesto")