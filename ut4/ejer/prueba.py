# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

def read_file(operations_path: Path):
    operations = [operation for operation in open(operations_path)]

def restock(operation: list, stock: dict):
    code = operation[1]
    qty_restock = int(operation[2])
    if code not in stock:
        stock[code] = qty_restock
    else:
        stock[code] += qty_restock

def change_price(operation: list, prices: dict):
    code = operation[1]
    new_price = int(operation[2])
    prices[code] = new_price
    
def reload_money(operation:list, money: int):
    money += int(operation[1])   

def run(operations_path: Path) -> bool:
    status_path = 'data/vending/status.dat'
    stock = {}
    prices = {}
    money = 0
    operations = read_file(operations_path)
    for operation in operations:
        match operation[0]:
            case 'R':
                restock(operation,stock)
            case 'P':
                change_price(operation,prices)
            case 'M':
                reload_money(operation,money)

    return filecmp.cmp(status_path, 'data/vending/.expected', shallow=False)


if __name__ == '__main__':
    run('data/vending/operations.dat')