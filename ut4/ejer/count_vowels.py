# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************

# RECURSIVIDAD
def count_vowels(text: str, num_vowels=0) -> int:
    VOWELS = "aeiou"
    if len(text) > 0:
        if text[0] in VOWELS:
            num_vowels += 1
    else:
        return num_vowels    
    return count_vowels(text[1:],num_vowels)

