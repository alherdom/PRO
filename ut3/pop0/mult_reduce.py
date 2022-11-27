# ************************
# MULTIPLICACI�N EN CADENAx
# ************************


def run(numbers: list) -> int:
    rmult = 1
    if len(numbers) > 1:
        rmult = numbers[0]*numbers[1]
        for value in numbers[2:]:
            rmult *= value
    return rmult


if __name__ == '__main__': 
    run([1, 2, 3, 4])
