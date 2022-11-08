# A partir de un texto confuso, eliminar todos los números.
# Tu programa tomará una cadena y limpiará todos los caracteres
# numéricos, # y devolverá una cadena con el espaciado y los
# caracteres especiales ~#$%^&!@*():;"',? todo intacto.

text = ("This looks5 grea8t! 123456789Bien!")
correct_text = ""
for letter in text:
    if letter.isnumeric():
        correct_text += ""
    else:
        correct_text+= letter     
print(correct_text)