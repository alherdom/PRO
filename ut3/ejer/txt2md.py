# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    md_path = 'data/txt2md/outline.md'
    output = ""
    simbol = "#"
    space = " "
    num_pad = 0
    with open('data/txt2md/outline.txt') as f:
        for line in f:
            len1 = len(line)
            len2 = len(line.strip())
            num_pad = len1 - len2
            output += simbol * num_pad + space + line.strip() + "\n"
    
    with open(md_path, "w") as result:
        result.write(output)   
            

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')