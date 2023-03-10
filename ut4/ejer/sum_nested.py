# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items:list) -> int:
    _sum = 0
    for item in items:
        if type(item) == list:
            _sum += sum_nested(item)
        else:
            _sum += item
    return _sum

