# ***************
# CUADRADO MÁGICO
# ***************


def is_magic_square(values: list) -> bool:
    
    if len(values) > 0:
        for value in values:
            sum_rows = [sum(value) for value in values]
            avg_rows = sum(sum_rows) / len(sum_rows)
            if avg_rows != sum(values[0]):
                return False
    return True
        

