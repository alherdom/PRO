# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

def read_file(operations_path:str):
    return (line.strip().split() for line in open(operations_path))

def restock(operation:list, stock:dict):
    code = operation[1]
    qty_restock = int(operation[2])
    if code not in stock:
        stock[code] = qty_restock
    else:
        stock[code] += qty_restock
    print(f'✅ {" ".join(operation)}')

def change_price(operation:list, stock:dict, prices:dict):
    code = operation[1]
    if code in stock:
        new_price = int(operation[2])
        prices[code] = new_price
        print(f'✅ {" ".join(operation)}')
    else:
        print(f'❌ {" ".join(operation)} (E1: PRODUCT NOT FOUND)')

def order(operation:list, stock:dict, prices:dict, money:int=0) -> int:
    code = operation[1]
    qty_ordered = int(operation[2])
    user_money = int(operation[3])
    if code in stock:
        if stock[code] >= qty_ordered:
            if user_money >= prices[code] * qty_ordered:
                stock[code] -= qty_ordered
                money += prices[code] * qty_ordered
                print(f'✅ {" ".join(operation)}')
            else:
                print(f'❌ {" ".join(operation)} (E3: NOT ENOUGH USER MONEY)')
        else:
            print(f'❌ {" ".join(operation)} (E2: UNAVAILABLE STOCK)')
    else:
        print(f'❌ {" ".join(operation)} (E1: PRODUCT NOT FOUND)')
    return money

def reload_money(operation:list, money:int=0) -> int:
    money += int(operation[1])
    print(f'✅ {" ".join(operation)}')
    return money

def write_file(status_path:Path, money:int, stock:dict, prices:dict):
     with open(status_path, "w") as f:
        f.write(f"{money}\n")
        for code_stock, code_price in zip(sorted(stock.items()), sorted(prices.items())):
            scode, stock = code_stock
            pcode, price = code_price
            f.write(f'{scode} {stock} {price}\n')

def run(operations_path: Path, money:int=0, stock:dict={}, prices:dict={}) -> bool:
    status_path = "data/vending/status.dat"
    operations = read_file(operations_path)
    for operation in operations:
        match operation[0]:
            case "R":
                restock(operation, stock)
            case "P":
                change_price(operation, stock, prices)
            case "O":
                money += order(operation, stock, prices)
            case "M":
                money += reload_money(operation)
    write_file(status_path, money, stock, prices)

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
