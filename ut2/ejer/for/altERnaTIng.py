#  Programe una solución que convierta cada letra minúscula en mayúscula y
# cada letra mayúscula se convierta en minúscula.
text = input("TECLE CUALQUIER FRASE USANDO MAYÚSCULAS Y MINUSCULAS: ")
save_str = ""
for letter in text:
    if letter.isupper():
        save_str += letter.lower()
    else:
        save_str += letter.upper()
print(save_str)