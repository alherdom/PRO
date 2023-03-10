# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


# def sum_nested(items: list, _sum:int=0) -> int:
#     if len(items) > 0:
#         if isinstance(items[1], list):
#             items[1] = sum(items[1])
#             return sum_nested(items[1::2],_sum)
#         else:
#             _sum = items[0] + (sum(items[1]))
#             return sum_nested(items[1::2],_sum)
#     return _sum

def sum_nested(items:list) -> int:
    for item in items:
        if type(item) == list:
            sum_nested(item)
        else:
            flat_list.append(item)
    return sum(flat_list)
flat_list = []

