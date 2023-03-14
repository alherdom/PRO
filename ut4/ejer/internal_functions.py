# Funciones interiores.
# Está permitido definir una función dentro de otra función:

VALID_CHARS = 'xyz'

def validation_rate(text: str) -> float:
    '''Rate of valid chars in text.'''
    def is_valid_char(char: str) -> bool:
        return char in VALID_CHARS
    checklist = [is_valid_char(c) for c in text]
    return sum(checklist) / len(text)

print(validation_rate('zxyzxxyz'))
# 1.0
# validation_rate('abzxyabcdz')
# 0.4
# validation_rate('abc')
# 0.0