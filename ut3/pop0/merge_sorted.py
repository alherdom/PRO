# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    merged = values1 + values2
    output = []
    for num in merged:
        if num not in output:
            output.append(num)
    merged = sorted(output)
    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
