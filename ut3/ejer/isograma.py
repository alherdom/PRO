# Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
# Ejemplos válidos de isogramas:
# lumberjacks
# background
# downstream
# six-year-old

# words = ["lumberjacks", "background", "downstream", "six-year-old"]
seen_chars = []
text = "teclado"
position = 0
for char in text.lower():
    if char in seen_chars:
        print("No es un isograma")
        break
    if char.isalpha():
        seen_chars.append(char)
else:
    print("✅ Es un isograma")
