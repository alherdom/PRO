OPERATION_PATH = 'ut4//te1/data/vending/operations.dat'
with open(OPERATION_PATH) as f:
    operations_list = []
    for line in f:
        operations_list.append(line.strip().split())
         
status = {}
money = 0
for operation in operations_list:
    match operation[0]:
        case "R":
            status[operation[1]] = [operation[2]] 
        case "P":
            for product, stock in status.items():
                status[product] = [stock[0],operation[2]]
        case "M":
            money += int(operation[1])
        case "O":
            insert_money = operation[3]
            print(status.get(operation[1], '❌ E1 PRODUCT NOT FOUND'))

STATUS_PATH = 'ut4/te1/data/vending/status.dat'     
with open(STATUS_PATH, 'w') as f:
    f.write(f'{money}\n')
    for product, state in sorted(status.items()):
        specs = ' '.join(str(i) for i in state) + "\n"
        f.write(f'{product} {specs}')

