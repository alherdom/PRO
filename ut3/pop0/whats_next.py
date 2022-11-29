# *********************
# ¿QUÉ ES LO SIGUIENTE?
# *********************


def run(items: list, ref_item: object) -> object:
    if not ref_item in items or ref_item == len(items):
        target_item = None
    else:
        ref_index = items.index(ref_item)
        for item in items:
            if items.index(item) > ref_index:     
                break
        target_item = item
               
    return target_item


if __name__ == '__main__':
    run([1, 2, 3, 4, 5, 6, 7], 3)
