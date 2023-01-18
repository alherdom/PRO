# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    values = list(items.values()) or [0]
    num_same_items = values.count(values[0])
    all_same = num_same_items == len(values)
    return all_same

    

if __name__ == "__main__":
    run({"a": 1, "b": 1, "c": 1, "d": 1})
