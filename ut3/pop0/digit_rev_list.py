# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    rev_digits = [int(value) for value in str(number)]
    rev_digits = list(reversed(rev_digits))
    return rev_digits


if __name__ == '__main__':
    run(35231)
