# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    inventory = {}
    imoves = imoves.split(",")
    oper = 0
    for imove in imoves:
        letter = imove[0]
        number = int(imove[1:])
        inventory[letter] = number
        if imove in inventory[letter]:
            oper += int(number)
            inventory[letter] = oper
        oper = 0
   
       
      
    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')

