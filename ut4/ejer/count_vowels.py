# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************

# RECURSIVIDAD
# def count_vowels(text: str, num_vowels=0) -> int:
#     VOWELS = "aeiou"
#     if len(text) > 0:
#         if text[0] in VOWELS:
#             num_vowels += 1
#     else:
#         return num_vowels    
#     return count_vowels(text[1:],num_vowels)

def count_vowels(text: str) -> int:
    VOWELS = "aeiou"
    if len(text) == 1:
        if text[0] in VOWELS:
            return 1
        return 0    
    return count_vowels(text[0]) + count_vowels(text[1:])