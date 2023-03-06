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
    result = {'money':total_bills,'products':stocks}
    return result

def reload_money(operation: list, machine_money: int) -> int:
    machine_money += int(operation[1])
    return machine_money

def run(operations_path: Path) -> bool:
    
    elements = []
    
    for operation in operations_list:
        match operation[0]:
            case "R":
                restocking(operation)
            case "P":
                pricing(operation)
            case "O":
                if operation[1] in status:
                    if status[operation[1]] >= int(operation[2]):
                        if int(operation[3]) >= (
                            int(operation[2]) * prices[operation[1]]
                        ):
                            status[operation[1]] -= int(operation[2])
                            money += int(operation[2]) * prices[operation[1]]
                        else:
                            print("E3 NOT ENOUGH USER MONEY")
                    else:
                        print("E2 UNAVAILABLE STOCK")
                else:
                    print("E1 PRODUCT NOT FOUND")
                # ordering (operation, money)
            case "M":
                money += int(operation[1])
                # reloading(operation,money)
    for stock, price in zip(
        status.values(), prices.values()
    ):  # LISTO STOCK Y PRECIO PARA FORMAR STATUS
        elements.append([stock, price])
    for key, element in zip(status.keys(), elements):  # SE CREA EL DICT STATUS
        status[key] = element
    with open(STATUS_PATH, "w") as f:  # ESCRITURA FICHERO DE SALIDA
        f.write(f"{money}\n")
        for product, stock_price in sorted(status.items()):
            specs = " ".join(str(i) for i in stock_price) + "\n"
            f.write(f"{product} {specs}")

    return filecmp.cmp(STATUS_PATH, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
