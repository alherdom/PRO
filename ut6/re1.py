import re
# Escriba un programa en Python que encuentre todas las 
# palabras que comiencen por vocal en un texto dado.
text = 'Escriba, un programa en Python que encuentre todas las palabras que comiencen por vocal en un texto dado.'
regex = r'\b[aeiou]\w+'
words = re.findall(regex, text, re.I)
print(words)