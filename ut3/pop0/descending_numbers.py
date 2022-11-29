# ****************
# CONTEO REGRESIVO
# ****************


def run(n: int) -> list:
    rev_nums = sorted(([1 + num for num in range(n)]), reverse=True)
    return rev_nums


if __name__ == '__main__':
    run(5)
