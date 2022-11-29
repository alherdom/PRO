# *****************
# MENOR ID SIN USAR
# *****************


def run(ids: list) -> int:
    numbers = numbers.split(",")
    size = len(numbers)
    numbers = numbers[1:size-1]
    smallest_unused_id = " ".join(numbers)
    return smallest_unused_id


if __name__ == '__main__':
    run([3, 1, 8, 4, 9])
