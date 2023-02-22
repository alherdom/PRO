vending_path = 'ut4/te1/data/vending.dat'
operations_path = 'ut4/te1/data/operations.dat'

with open(vending_path, encoding="utf8") as f1, open(operations_path, encoding="utf8") as f2:
    coins = f1.readline().split()
    two_coin = coins[0]
    one_coin = coins[1]
    fifty_coin = coins[2]
    vending_list = f1.read().split()
    operations_list = f2.read().split()
    
    for operation in operations_list:
        if operation == 'O':
            print('Its Order')
        elif operation == 'R':
            print('Its Restock')
        elif operation == 'P':
            print('Its Price')
       
status_path = 'ut4/te1/data/status.dat'     
with open(status_path, 'w', encoding="utf8") as f3:
    f3.write(f'Hola')
