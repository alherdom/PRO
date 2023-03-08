# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

OPERATION_PATH = "data/vending/operations.dat"
STATUS_PATH = "data/vending/status.dat"   

def run(operations_path: Path) -> bool:
    money = 0
    elements = []
    prices = {}
    stocks = {}
    # LECTURA FICHERO DE ENTRADA
    operations_list = [line.strip().split() for line in open(OPERATION_PATH)]

    def restock(operation: list) -> dict:  # FUNCIÓN DE REASBASTECIMIENTO DE PRODUCTO
        if operation[1] in stocks:
            stocks[operation[1]] += int(operation[2])
        else:
            stocks[operation[1]] = int(operation[2])
        return stocks

    def change_price(operation: list) -> dict:  # FUNCIÓN PARA FIJAR PRECIOS
        if operation[1] in stocks:
            prices[operation[1]] = int(operation[2])
        else:
            print("E1 PRODUCT NOT FOUND")
        return prices

    def order(operation: list, money: int) -> tuple[dict, int]:  # FUNCIÓN PARA PEDIDOS EN LA MÁQUINA
        if operation[1] in stocks:
            if stocks[operation[1]] >= int(operation[2]):
                if int(operation[3]) >= (int(operation[2]) * prices[operation[1]]):
                    stocks[operation[1]] -= int(operation[2])
                    money += int(operation[2]) * prices[operation[1]]
                else:
                    print("E3 NOT ENOUGH USER MONEY")
            else:
                print("E2 UNAVAILABLE STOCK")
        else:
            print("E1 PRODUCT NOT FOUND")
        return (stocks, money)

    def reload_money(operation: list, money: int) -> int:  # FUNCIÓN PARA RECARGA DE DINERO
        money += int(operation[1])
        return money
    
    for operation in operations_list:
        match operation[0]:
            case "R":
                restock(operation)
            case "P":
                change_price(operation)
            case "O":
                (stocks, money) = order(operation, money)
            case "M":
                money = reload_money(operation,money)
                                
    for stock, price in zip(stocks.values(), prices.values()):  # LISTO STOCK Y PRECIO PARA FORMAR stocks
        elements.append([stock, price])
        
    for key, element in zip(stocks.keys(), elements):  # SE CREA EL DICT stocks
        stocks[key] = element
               
    with open(STATUS_PATH, "w") as f:  # ESCRITURA FICHERO DE SALIDA
        f.write(f"{money}\n")
        for product, stock_price in sorted(stocks.items()):
            specs = " ".join(str(i) for i in stock_price) + "\n"
            f.write(f"{product} {specs}")

    return filecmp.cmp(STATUS_PATH, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")

