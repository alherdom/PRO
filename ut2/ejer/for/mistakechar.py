# Dada una cadena de texto corregir los errores en el texto digitalizado.
# Los errores son los siguientes errores:
#  - La S se interpreta erróneamente como 5.
#  - La O se interpreta erróneamente como 0.
#  - I se interpreta erróneamente como 1.
#  - Los casos de prueba contienen números sólo por error.

text = ("J.R.R. T0LK1EN - THE L0RD 0F THE R1NG5")
correct_text = ""
for letter in text:
    if letter == "5":
        correct_text += "S"
    elif letter == "0":
        correct_text += "O"
    elif letter == "1":
        correct_text += "I"
    else:
        correct_text+= letter     
print(correct_text)