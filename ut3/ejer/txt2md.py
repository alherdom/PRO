# *******************
# DE TEXTO A MARKDOWN
# *******************
import filecmp
from pathlib import Path


def run(text_path: Path) -> bool:
    output = ""
    num_pad = 0
    md_path = 'data/txt2md/outline.md'
    with open('data/txt2md/outline.txt') as f:
        for line in f:
            num_pad = len(line) - len(line.strip())
            output += "#" * num_pad + " " + line.strip() + "\n"
    with open(md_path, "w") as result:
        result.write(output)   
            

    return filecmp.cmp(md_path, 'data/txt2md/.expected', shallow=False)


if __name__ == '__main__':
    run('data/txt2md/outline.txt')