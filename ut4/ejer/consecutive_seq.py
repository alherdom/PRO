# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

# SIN RECURSIVIDAD
# def consecutive_seq(items: list, target_count: list) -> int:
#     for item in items:
#         times = items.count(item)
#         if times == target_count:
#             return item
#     return False
        
# CON RECURSIVIDAD
def consecutive_seq(items: list, target_count: list, count=1):
    if len(items) == 1:
        return False
    if items[0] == items[1]:
        count += 1
    if target_count == count:
        return items[0]
    return consecutive_seq(items[1:], target_count, count)
    
