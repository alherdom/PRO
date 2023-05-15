class InfiniteList:
    '''Cree una clase InfiniteList que permita utilizar una 
    lista sin tener límites, es decir, evitando un IndexError. 
    Por ejemplo, si la lista tiene 10 elementos, y asignamos un
    valor al elemento en el índice 20, esto no daría un error, sino
    que haría ampliar la lista hasta el valor 20, rellenando los valores
    en blanco con el valor None.'''
    
    def __init__(self, *args, fill_value = None):
        self.fill_value = fill_value
        self.elements = list(args)
        
    def __len__(self):
        return len(self.elements)
        
    def __setitem__(self, index: int, value):
        if index > len(self.elements):
            for _ in range(len(self.elements), index + 1):
                self.elements.append(self.fill_value)
        self.elements[index] = value
            
    def __getitem__(self, index: int):
        return self.elements[index]
    
            
cosas = "pan","agua","lechuga","tomate"
compra = InfiniteList(cosas,"-")
compra[8] = 10
print(compra)

# class InfiniteList:
#     def __init__(self, *args, fill_value=None):
#         self.items = [item for item in args]
#         self.fill_value = fill_value

#     def __getitem__(self, index: int):
#         return self.items[index]

#     def __len__(self):
#         return len(self.items)

#     def __setitem__(self, index: int, item) -> None:
#         if index >= len(self):
#             for _ in range(len(self), index + 1):
#                 self.items.append(self.fill_value)
#         self.items[index] = item

#     def __str__(self):
#         to_show = [str(element) for element in self.items]
#         return ",".join(to_show)