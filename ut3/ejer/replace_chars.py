# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool: 
    with open(input_path, encoding="utf8") as finput:
        i = 0
        old_chars = []
        new_chars = []
        news = finput.read()
        replace_chars = replacements.replace("|","").split
        old_chars.append(replace_chars[::2])
        new_chars.append(replace_chars[1::2])
        print(new_chars)
        for old_char, new_char in zip(old_chars,new_chars):
            print(old_char)
            print(new_char)
            news = news.replace(old_char,new_char)
   
        
    output_path = 'data/replace_chars/r_noticia.txt'
    with open(output_path, 'w',encoding="utf8") as foutput:
        foutput.write(news)
    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', '�a|�e|�i|�o|�u')