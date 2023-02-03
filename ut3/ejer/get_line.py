# *****************
# HAN CANTADO L�NEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    with open(input_path, encoding="utf8") as f1:
        line = None
        count = 0
        for line_f1 in f1:
            count += 1
            if count == line_no:
                line = line_f1.strip()
                break

    return line


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)