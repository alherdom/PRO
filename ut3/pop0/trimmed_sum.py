# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    if len(values) > 0:
        max_number = max(values)
        min_number = min(values)
        while max_number in values:
            values.remove(max_number)
        while min_number in values:
            values.remove(min_number)
    tsum = sum(values)

  
    return tsum


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])
