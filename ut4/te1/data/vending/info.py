# order:
#   - comprobar si existe el pedido
#   - comprobar que hay stock suficiente
#   - comprobar que el dinero que se ha pagado cubre lo que se ha pedido, que no se haya pagado de menos.
#     - sumar al dinero y restar las unidades del stock


# def order(nameOrder):
#   has_the_product(nameOrder)
#   is_product_available(nameOrder)
#   has_user_enough_money(nameOrder)


# run():
#   readFile('path')
#   executeMachine(operations)
#     executeOperation(operation)
#       checkOperation
#       ....
#       ....
#   writeResultMachineInFile(nameFile)

# clase bici
#   clase rueda
#   clase chasis
#   clase sillin
#   clase manillar

result: {'productA':(stock, price)},{'productB':(stock,price)},{'productC':(stock,price)}


D12 R 7

readFile -> [
  {
    operation
    product
    cost
  }
]

maquina(operations -> dict[str, str, int])


class animal:
  def sonido(self):
    pass

class perro(animal):
  def sonido(self):
    print('guau')

class gato(animal):
  def sonido(self):
    print('miau')


miGato = gato()
miGato.