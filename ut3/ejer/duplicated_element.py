# Escriba un programa en Python que acepte una lista y elimine sus elementos duplicados.
# Entrada: ['this', 'is', 'a', 'real', 'real', 'real', 'story']
# Salida: ['this', 'is', 'a', 'real', 'story']

text = ["this", "is", "a", "real", "real", "real", "story"]
clean_text = []
for words in text:
    if words == text[1:]:
        print("No es igual")
    else:
        clean_text += words
        print(clean_text)
