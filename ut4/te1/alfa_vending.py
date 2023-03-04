OPERATION_PATH = "ut4//te1/data/vending/operations.dat"
with open(OPERATION_PATH) as f:
    operations_list = [line.strip().split() for line in f]

money = 0
elements = []
prices = {}
status = {}
for operation in operations_list:
    match operation[0]:
        case "R":        
            status[operation[1]] = int(operation[2])
        case "P":
            price = int(operation[2])
            if operation[1] in status:
                prices[operation[1]] = int(operation[2])
            else:
                print('E1 PRODUCT NOT FOUND')
        case "O":
            if operation[1] in status:
                paid = int(operation[3])
                order = int(operation[2])
                product = operation[1]
                price = prices[operation[1]]
                print(price)
                bill = order * price
        case "M":
            money += int(operation[1])

for stock, price in zip(status.values(), prices.values()):
    elements.append([stock, price])

for key, element in zip(status.keys(), elements):
    status[key] = element


STATUS_PATH = "ut4/te1/data/vending/status.dat"
with open(STATUS_PATH, "w") as f:
    f.write(f"{money}\n")
    for product, stock_price in sorted(status.items()):
           specs = " ".join(str(i) for i in stock_price) + "\n"
           f.write(f"{product} {specs}")
