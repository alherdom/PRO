# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


# def consecutive_seq(items: list, target_count: list) -> int:
#     for item in items:
#         times = items.count(item)
#         if times == target_count:
#             return item
#     return False
        
def consecutive_seq(items: list, target_count: list, i: int) -> int:
    i = 1
    count = 0
    if items[:i] == items[:i+1]:
        count +=1
    if count == target_count:
        return items[:i]
    return False

