# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    with open(input_path, encoding="utf8") as finput:
        news = finput.read()
        if "á" in news:
            news = news.replace("á", "a")
        if "é" in news:
            news = news.replace("é", "e")
        if "í" in news:
            news = news.replace("í", "i")
        if "ó" in news:
            news = news.replace("ó", "o")
        if "ú" in news:
            news = news.replace("ú", "u")
    output_path = 'data/replace_chars/r_noticia.txt'
    with open(output_path, 'w',encoding="utf8") as foutput:
        foutput.write(news)
    
    
        
    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', '�a|�e|�i|�o|�u')