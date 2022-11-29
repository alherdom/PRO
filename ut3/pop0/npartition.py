# ***********************
# PARTICIÓN POR EL NÚMERO
# ***********************


def run(values: list, ref_value: int) -> list:
    min_values = []
    max_values = []
    npartition = []
    for value in values:
        if value >= ref_value:
            max_values.append(value)
        else:
            min_values.append(value)
    npartition.append(min_values)
    npartition.append(max_values)
    return npartition


if __name__ == '__main__':
    run([4, 3, 2, 9, 8, 5], 4)
