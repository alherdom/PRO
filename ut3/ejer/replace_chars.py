# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool: 
    replacements = replacements.split('|')
    with open(input_path, encoding="utf8") as finput:    
        news = finput.read()
        
        for old_char, new_char in zip(old_chars,new_chars):
            news = news.replace(old_char,new_char)
   
        
    output_path = 'data/replace_chars/r_noticia.txt'
    with open(output_path, 'w',encoding="utf8") as foutput:
        foutput.write(news)
    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', '�a|�e|�i|�o|�u')