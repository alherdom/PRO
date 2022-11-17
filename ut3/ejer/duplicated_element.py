# Escriba un programa en Python que acepte una lista y elimine sus elementos duplicados.
# Entrada: ['this', 'is', 'a', 'real', 'real', 'real', 'story']
# Salida: ['this', 'is', 'a', 'real', 'story']

text = ["this", "is", "a", "real", "real", "real", "story"]
cleaned_text = []
for words in text:
    if words not in cleaned_text:
        cleaned_text.append(words)
print(cleaned_text)
