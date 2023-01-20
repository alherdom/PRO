# **********************
# BORRANDO VALORES CLAVE
# **********************


def run(items: dict) -> dict:
    # TU CÓDIGO AQUÍ
    citems = {}
    
    citems = {keys: [] for keys in items.keys()}
    
    """
    for item, value in items.items():
        key = item
        value = []  
        citems[key] = value  
    """
      
    
    
    return citems


if __name__ == '__main__':
    run({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]})
