# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
    again = True
    sorted_items = items.copy()
    while again:
        again = False
        for i in range(len(sorted_items)-1):
            if sorted_items[i] > sorted_items[i+1]:
                sorted_items[i], sorted_items[i+1] = sorted_items[i+1], sorted_items[i]
                again = True
           
                        
    return sorted_items
    

