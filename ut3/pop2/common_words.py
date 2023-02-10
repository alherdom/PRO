# *************************
# BUSCANDO PALABRAS COMUNES
# *************************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:

    with open(input_path) as f:
        lines = f.readlines()
        sentences = [line.lower().strip().split() for line in f]

        output_path = "data/common_words/output.txt"
        with open(output_path, "w") as f:
            f.write("Hola")

    return filecmp.cmp(output_path, "data/common_words/.expected", shallow=False)


if __name__ == "__main__":
    run("data/common_words/minizen.txt")
