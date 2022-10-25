# Escriba un programa que pida nombre y apellidos de una persona (único input) y
# repita la pregunta mientras el nombre no esté en formato título.
name = input("¿Su nombre? ")
while not name.istitle():
    print("Error. Debe escribirlo correctamente")
    name = input("¿Su nombre? ")
else:
    print(name)
