# ************
# ELLA QUÍMICA
# ************


def run(formula: list) -> bool:
    size_formula = len(formula)
    valid = True
    if 1 and 2 in formula:
        valid = False
    if 5 in formula and not 6 in formula:
        valid = False       
    if 6 in formula and not 5 in formula:
        valid = False
    return valid


if __name__ == '__main__':
    run([1, 3, 7])
