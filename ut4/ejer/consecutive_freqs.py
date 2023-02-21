# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items,as_string=False):
    freqs = []
    elements = []_
    quantitys = []
    i = 0
    count = 0
    for item in items:
        if item not in elements:
            elements.append(item)
        if items[i] == item:
            count += 1
        if items.index(item) == len(items)
            quantitys.append(count)
            i += 1
            count = 0
    print(elements)
    print(quantitys)
    
    if as_string:
        return ''   
    
    return freqs                    
    

