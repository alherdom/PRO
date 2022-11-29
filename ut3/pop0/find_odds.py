# ********************
# DESCUBRIENDO IMPARES
# ********************


def run(values: list) -> list:
    odds = []
    for value in values:
        if value % 2 != 0 and value not in odds:
            odds.append(value)    
    
    return odds


if __name__ == '__main__':
    run([1, 2, 3, 4, 5])
