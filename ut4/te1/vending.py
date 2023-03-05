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
    status = {}
    
    f = open(OPERATION_PATH)                                    # LECTURA FICHERO DE ENTRADA
    operations_list = [line.strip().split() for line in f]
    
    def restocking(operation: list) -> dict:                    # FUNCIÓN DE REASBASTECIMIENTO DE PRODUCTO
        if operation[1] in status:
            status[operation[1]] += int(operation[2])
        else:
            status[operation[1]] = int(operation[2])
        return status
    
    def pricing(operation: list) -> dict:                       # FUNCIÓN PARA FIJAR PRECIOS
        if operation[1] in status:
                    prices[operation[1]] = int(operation[2])
        else:
            print("E1 PRODUCT NOT FOUND")
        return prices
    
    def ordering(operation: list, money: int) -> dict:          # FUNCIÓN PARA PEDIDOS EN LA MÁQUINA
        if operation[1] in status:
            if status[operation[1]] >= int(operation[2]):
                if int(operation[3]) >= (int(operation[2]) * prices[operation[1]]):
                    status[operation[1]] -= int(operation[2])
                    money += int(operation[2]) * prices[operation[1]]
                else:
                    print("E3 NOT ENOUGH USER MONEY")
            else:
                print("E2 UNAVAILABLE STOCK")
        else:
            print("E1 PRODUCT NOT FOUND")
        return status
    
    def reloading(operation: list, money: int) -> int:          # FUNCIÓN PARA RECARGA DE DINERO
        money += int(operation[1])
        return money
    
    for operation in operations_list:
        match operation[0]:
            case "R":
                restocking (operation)
            case "P":
                pricing (operation)
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
                
    for stock, price in zip(status.values(), prices.values()):  # LISTO STOCK Y PRECIO PARA FORMAR STATUS
        elements.append([stock, price])

    for key, element in zip(status.keys(), elements):           # SE CREA EL DICT STATUS
        status[key] = element

    with open(STATUS_PATH, "w") as f:                           # ESCRITURA FICHERO DE SALIDA
        f.write(f"{money}\n")
        for product, stock_price in sorted(status.items()):
            specs = " ".join(str(i) for i in stock_price) + "\n"
            f.write(f"{product} {specs}")

    return filecmp.cmp(STATUS_PATH, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
