import sys

import pycheck


def run(text: str) -> str:
    # Escribe un programa en Python que, dada una cadena de texto, elimine todas las vocales SIN UTILIZAR LA FUNCIÓN replace().
    VOWELS = "aeiou"
    output = ""
    for letter in text:
        if letter.lower() not in VOWELS:
            output += letter

    return output


if __name__ == "__main__":
    pycheck.check("pro.ut2.pop0.ej1", sys.argv, run)
