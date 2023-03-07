# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    text = text.replace(" ","").lower()
    for char1, char2 in zip(text, text[::-1]):
        if char1 == char2:
            return True    
        return False

