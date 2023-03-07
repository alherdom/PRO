names = ["ana", "pepa", "maria"]

def sum_len_names(names: list) -> int:
    size = len(names[1])
    return sum_len_names(names)


print(sum_len_names(names))
