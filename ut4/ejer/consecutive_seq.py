# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items: list, target_count: list) -> int:
    for item in items:
        times = items.count(item)
        if times == target_count:
            return item
    return False
        

