# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    oper = 0
    numbers = []

    for char in imoves:
        if char.isalpha():
            inventory[char] = []
        if char.isdigit():
            oper += int(char)
            numbers.append(char)    
    print(numbers)
    print(oper)         
         
    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')

