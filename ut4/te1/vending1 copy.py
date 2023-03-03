OPERATION_PATH = 'ut4//te1/data/vending/operations.dat'
with open(OPERATION_PATH, encoding="utf8") as f:
    operations_list = []
    for line in f:
        line = line.strip().split()
        operations_list.append(line)
         
status = {}
money = 0
for operation in operations_list:
    match operation[0]:
        case "R":
            status[operation[1]] = [operation[2]] 
        case "P":
            for product, stock in status.items():
                if operation[1] == product:
                    values = [stock[0],operation[2]]
                    status[product] = values
        case "M":
            money += int(operation[1])
        case "O":
            print(operation)
        
STATUS_PATH = 'ut4/te1/data/vending/status.dat'     
with open(STATUS_PATH, 'w', encoding="utf8") as f:
    f.write(f'{money}\n')
    for product, state in sorted(status.items()):
        specs = ' '.join(str(i) for i in state) + "\n"
        f.write(f'{product} {specs}')

