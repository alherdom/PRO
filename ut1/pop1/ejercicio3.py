# ut1-pop1-ej3
VOWELS = 'aeiou'
target_vowel = 'e'
target_offset = 2
input_text = 'Hay una gran diferencia entre conocer el camino y andar el camino'
# No tocar nada de aquí hacia arriba ↑
# ********************************************************

# ========================================================
# @@ Escribe tu código debajo de esta línea ↓
position_target_vowel = VOWELS.find(target_vowel)
position_vowel_offset = position_target_vowel + target_offset
vowel_offset = VOWELS[position_vowel_offset]
output_text = input_text.replace(target_vowel, vowel_offset)
# $$ Escribe tu código encima de esta línea ↑
# ========================================================

# ********************************************************
# No tocar nada de aquí hacia abajo ↓
assert output_text == 'Hay una gran diforoncia ontro conocor ol camino y andar ol camino'