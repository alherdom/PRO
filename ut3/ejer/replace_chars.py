# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    chars = replacements.split("|")
    with open(input_path) as f1:
        noticia = f1.read()
        for old_char, new_char in chars:
            noticia = noticia.replace(old_char,new_char)
    output_path = "data/replace_chars/r_noticia.txt"
    with open(output_path, "w") as freplaced:
        freplaced.write(noticia)



    return filecmp.cmp(output_path, "data/replace_chars/.expected", shallow=False)


if __name__ == "__main__":
    run("data/replace_chars/noticia.txt", "�a|�e|�i|�o|�u")
