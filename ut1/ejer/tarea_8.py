#Escriba un programa en Python que acepte una palabra en castellano y calcule una métrica
# que sea el número total de caracteres de la palabra multiplicado por el número total
# de vocales que contiene la palabra.
#Entrada: ordenador Salida: 36
word = input('Teclea una palabra: ')
len_word = len(word)
count_a = word.count('a')
count_e = word.count('e')
count_i = word.count('i')
count_o = word.count('o')
count_u = word.count('u')
total_vowels = count_a + count_e + count_i + count_o + count_u 
print(total_vowels * len_word)
