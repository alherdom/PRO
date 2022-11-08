# Escriba un programa en Python que acepte 3 códigos de teclas y muestre por pantalla la acción que se lleva a cabo en sistemas Ubuntu Linux.
# Entrada: tecla1=Ctrl; tecla2=Alt; tecla3=Del;
# Salida: Log out
tecla1 = int(input("Pulse la primera tecla: "))
tecla2 = int(input("Pulse la segunda tecla: "))
tecla3 = int(input("Pulse la tercera tecla: "))
combinacion = tecla1, tecla2, tecla3
match combinacion:
        case "+":
            result = number_1 + number_2
        case "-":
            result = number_1 - number_2
        case "*":
            result = number_1 * number_2
        case "/":
            result = number_1 / number_2
        case _:
            result = None
            print("OPERANDO INCORRECTO, ESCOJA UNA DE LOS SIGUIENTE(+,-,*,/)")
if result is None:
    print("Algo va mal")
else:
    print(f"{number_1}{oper}{number_2}={result}")
