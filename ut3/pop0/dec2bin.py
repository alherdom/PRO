'''
Convierta un número decimal entero a su representación binaria (como string).
'''


def run(num: int) -> str:
    conversion = []
    while num >= 1:
        conversion.append(str(num % 2))
        num //= 2
    to_bin = "".join(conversion[::-1])
    return to_bin


if __name__ == '__main__':
    run(1)
