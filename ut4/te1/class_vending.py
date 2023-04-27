# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

class Vending:
    
    def __init__(self) -> None:
        pass
    
    
    def read_file(self, path: str):
        return (line.strip().split() for line in open(path))


    def restock(self, operation: list, vending_status: dict):
        code = operation[1]
        restock_qty = int(operation[2])
        products = vending_status["products"]
        if code in products:
            details = products[code]
            details["stock"] += restock_qty
        else:
            details = {"stock": restock_qty, "price": 0}
            products[code] = details


    def change_price(self, operation: list, vending_status: dict):
        code = operation[1]
        new_price = int(operation[2])
        products = vending_status["products"]
        if code in products:
            details = products[code]
            details["price"] = new_price


    def order(self, operation: list, vending_status: dict):
        code = operation[1]
        qty_ordered = int(operation[2])
        user_money = int(operation[3])
        products = vending_status["products"]
        if code in products:
            details = products[code]
            stock, price = details.values()
            if (user_money >= price * qty_ordered) and (stock >= qty_ordered):
                vending_status["money"] += price * qty_ordered
                details["stock"] -= qty_ordered


    def reload_money(self, operation: list, vending_status: dict):
        vending_status["money"] += int(operation[1])


    def write_file(self, path: Path, vending_status: dict):
        with open(path, "w") as f:
            money = vending_status["money"]
            products = vending_status["products"]
            f.write(f"{money}\n")
            for code, details in sorted(products.items()):
                details_list = " ".join((str(detail) for detail in details.values()))
                f.write(f"{code} {details_list}\n")


def run(operations_path: Path, self) -> bool:
    STATUS_PATH = "data/vending/status.dat"
    vending_status = {"money": 0, "products": {}}
    operations = self.read_file(operations_path)

    for operation in operations:
        match operation[0]:
            case "O":
                self.order(operation, vending_status)
            case "R":
                self.restock(operation, vending_status)
            case "P":
                self.change_price(operation, vending_status)
            case "M":
                self.reload_money(operation, vending_status)

    self.write_file(STATUS_PATH, vending_status)

    return filecmp.cmp(STATUS_PATH, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")