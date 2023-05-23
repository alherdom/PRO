import re

# Escriba un programa en Python que encuentre todas las URLs en un texto dado.

text = 'http://aprendepython.es/stdlib/text_processing/re/ hola esta es la pagina de aprende python https://github.com/alherdom?tab=repositories esta es la pagina de GitHub'
regex = r'https?://\S+'
words = re.findall(regex, text)
print(words)