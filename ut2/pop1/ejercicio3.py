import sys

import pycheck

CHECK_CASES = [
    [["AGTCCCAGGT"], "AGUCCCAGGU"],
    [["GCGCACTCTTCTTTGCTCTT"], "GCGCACUCUUCUUUGCUCUU"],
    [["CCGGAGATTGGCTACTGAAGATCCA"], "CCGGAGAUUGGCUACUGAAGAUCCA"],
]


def run(adn: str) -> str:
    arn = ""
    for letter in adn:
        if letter == "T":
            arn += "U"
        else:
            arn += letter
    return arn


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
