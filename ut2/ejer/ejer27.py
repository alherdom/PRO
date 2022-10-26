# Escriba un programa en Python que acepte dos cadenas de texto y
# compute el producto cartesiano letra a letra entre ellas.
str1 = "abc"
str2 = "123"
for char1 in str1: # Iteramos caracter por caracter en la primera cadena de texto.
    for char2 in str2: # Dentro de la iteración de la primera cade,a de texto, volvemos a iterar caracter por caracter en la segunda cadena de texto.
        print(f'{char1}{char2}', end=" ") # Muestro por pantalla caracter con caracter, y añado el end=" " para separarlos con un espacio y colocar en línea.
