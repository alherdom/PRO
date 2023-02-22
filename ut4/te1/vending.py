vending_path = 'ut4/te1/data/vending.dat'
operations_path = 'ut4/te1/data/operations.dat'

with open(vending_path, encoding="utf8") as f1, open(operations_path, encoding="utf8") as f2:
    vending_list = f1.read().split()
    operations_list = f2.read().split()
    print(vending_list)
    print(operations_list)
       
status_path = 'ut4/te1/data/status.dat'     
with open(status_path, 'w', encoding="utf8") as f3:
    f3.write(f'Hola')
