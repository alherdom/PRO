# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    NOT_VALID_CHAR='aeiouAEIOU '
    cconst = ""

    
    """for char1 in text1:
        if char1 in text2 and char1 not in VOWELS and char1 not in cconst:
            cconst+= char1
            cconst = ''.join(sorted(cconst))"""

    
    cconst = {char1 for char1 in text1 if char1 in text2 and char1 not in NOT_VALID_CHAR}
    cconst = ''.join(sorted(cconst))
    
    
    
    return cconst


if __name__ == '__main__':
    run('Flat is better than nested', 'Readability counts')