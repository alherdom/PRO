# Tareas básicas de regex. Escriba una función que tome un código numérico de cualquier longitud.
# La función debe comprobar si el código empieza por 1, 2 o 3 y devolver true si es así. En caso
# contrario, devolverá false.
START = "123"
num_cod = input("TECLEE EL CÓDIGO NUMERICO: ")
if num_cod[0] in START:
    print("True")
else:
    print("False")

