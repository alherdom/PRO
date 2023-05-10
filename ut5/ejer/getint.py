# Sabiendo que ValueError es la excepción que se lanza cuando no podemos 
# convertir una cadena de texto en su valor numérico, escriba una función 
# getint() que lea un valor entero del usuario y lo devuelva, iterando 
# mientras el valor no sea correcto.

# Ejecución a modo de ejemplo:

# Give me an integer number: ten
# Not a valid integer. Try it again!
# Give me an integer number: diez
# Not a valid integer. Try it again!
# Give me an integer number: 10
# Trate de implementar tanto la versión recursiva como la versión iterativa.

# def getint():
#     while True:
#         value = int(input("Give me an integer number: "))
#         try:
#             return f"It's ok {value} is a integer"
#         except ValueError:
#             print("Not a valid integer. Try it again!")

def getint():
    try:
        value = int(input("Give me an integer number: "))
    except ValueError:
        print("Not a valid integer. Try it again!")
        getint()
    else:
        print(f"It's ok {value} is a integer")

getint()