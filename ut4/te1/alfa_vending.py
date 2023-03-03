OPERATION_PATH = 'ut4//te1/data/vending/operations.dat'
with open(OPERATION_PATH) as f:
    operations_list = [line.strip().split() for line in f]
    
money = 0        
status = {}
for operation in operations_list:
    match operation[0]:
        case "R":
            status[operation[1]] = [operation[2]] 
        case "P":
            for product, element in status.items():
                status[product] = [element[0],operation[2]]
        case "M":
            money += int(operation[1])
        case "O":
            order_stock = int(operation[2])
            insert_money = int(operation[3])
            # print(status.get(operation[1], '❌ E1 PRODUCT NOT FOUND'))
            for product, element in status.items():
                status[product] = [int(element[1])-order_stock,int(operation[2])-insert_money]
                                 
                      
            
STATUS_PATH = 'ut4/te1/data/vending/status.dat'     
with open(STATUS_PATH, 'w') as f:
    f.write(f'{money}\n')
    for product, state in sorted(status.items()):
        specs = ' '.join(str(i) for i in state) + "\n"
        f.write(f'{product} {specs}')

