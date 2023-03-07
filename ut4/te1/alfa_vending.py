# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

OPERATION_PATH = "data/vending/operations.dat"
STATUS_PATH = "data/vending/status.dat"

def read_operations(operation_path:str) -> list:
    operations_list = [line.strip().split() for line in open(OPERATION_PATH)]
    return operations_list

def restock(operation: list, stocks: dict) -> dict:
    product = operation[1]
    stock = int(operation[2]) 
    if operation[1] in stocks:
        stocks[product] += stock
    else:
        stocks[product] = stock
    return stocks
    
def change_price(operation: list, stocks:dict, prices: dict) -> dict:
    product = operation[1]
    price = int(operation[2])
    if product in stocks:
        prices[product] = price
    return prices

def order(operation: list, stocks: dict, prices: dict) -> dict:
    total_bills = 0
    product = operation[1]
    qty_ordered = int(operation[2])
    user_money = int(operation[3])
    if product in stocks:
        if stocks[product] >= qty_ordered:
            if user_money >= (qty_ordered * prices[product]):
                stocks[product] -= int(operation[2])
                total_bills += int(operation[2]) * prices[operation[1]]
    result = {'money':total_bills,'products':stocks,'prices':prices}
    return result

def reload_money(operation: list, machine_money: int, result: dict) -> dict:
    machine_money += int(operation[1])
    result['money'] += machine_money
    return result

def run(operations_path: Path) -> bool:
    total_bills = result[0]
    stocks = result[1]
    
    elements = []
    
    
    for operation in read_operations(OPERATION_PATH):
        match operation[0]:
            case "R":
                restock(operation)
            case "P":
                pricing(operation)
            case "O":             
                ordering(operation, money)
            case "M":
                reload_money(operation,machine_money,result)
                
    for stock, price in zip(
        stocks.values(), prices.values()
    ):  # LISTO STOCK Y PRECIO PARA FORMAR STATUS
        elements.append([stock, price])
        
    for key, element in zip(stocks.keys(), elements):  # SE CREA EL DICT STATUS
        stocks[key] = element
        
    with open(STATUS_PATH, "w") as f:  # ESCRITURA FICHERO DE SALIDA
        f.write(f"{money}\n")
        for product, stock_price in sorted(status.items()):
            specs = " ".join(str(i) for i in stock_price) + "\n"
            f.write(f"{product} {specs}")

    return filecmp.cmp(STATUS_PATH, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
