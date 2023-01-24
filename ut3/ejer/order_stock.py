# ***********
# ¿HAY STOCK?
# ***********


def run(stock: dict, merch: str, amount: int) -> bool:
    
    merch_stock = stock.get(merch,0)
    available = merch_stock >= amount
    
    """
    if stock[merch] >= amount:
        available = True
    """
    
    """for item, number in stock.items():
        if merch == item and amount <= number:
            available = True
            break
    """   
    return available


if __name__ == '__main__':
    run({'pen': 20, 'cup': 11, 'keyring': 40}, 'cup', 9)
