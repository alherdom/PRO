# Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos.
# Entrada: hello-world
# Salida: Se han encontrado caracteres no alfabéticos
entrada = "hello-world"
for letter in entrada:
    if not letter.isalpha():
        print("Se han encontrado caracteres no alfabéticos")
        break
else:
    print("Es alfabetico")
