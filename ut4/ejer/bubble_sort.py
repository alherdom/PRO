# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items):
    sorted_items = items.copy()
    for i in range(len(sorted_items)-1):
        if sorted_items[i] > sorted_items[i+1]:
            sorted_items[i], sorted_items[i+1] = sorted_items[i+1], sorted_items[i]
    

        
                
                
        
                
                      
       
    
    return sorted_items
    

