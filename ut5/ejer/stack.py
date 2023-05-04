from __future__ import annotations


class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.max_size= max_size
        self.items = []

    def push(self, item: int) -> bool:
        '''Si la pila está llena retornar False, en otro caso retornar True'''
        if len(self.items) == self.max_size:
            return False
        return True

    def pop(self) -> int:
        '''Extraer el elemento que está en el TOP de la pila'''
        return self.items.pop(0)

    def top(self) -> int:
        '''Devolver el elemento que está en el TOP de la pila (sin extracción)'''
        return self.items[0]

    def is_empty(self) -> bool:
        '''Indica si la pila está vacía'''
        if len(self.items) == 0:
            return True
        return False

    def is_full(self) -> bool:
        '''Indica si la pila está llena -> max_size'''
        if len(self.items) == self.max_size:
            return True
        return False

    def expand(self, factor: int = 2) -> None:
        '''Expande el tamaño máximo de la pila en el factor indicado'''
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        '''Vuelca la pila a un fichero. Cada item en una línea'''
        f = open(path, 'w')
        for item in self.items:
            f.write(item + '\n')
        
    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        '''Crea una pila desde un fichero. Si la pila se llena al ir añadiendo elementos
        habrá que expandir con los valores por defecto'''
        ...

    def __getitem__(self, index: int) -> int:
        '''Devuelve el elemento de la pila en el índice indicado'''
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        '''Establece el valor de un elemento de la pila mediante el índice indicado'''
        self.items[index] = item


    def __len__(self) -> int:
        '''Número de elementos que contiene la pila'''
        return len(self.items)

    def __str__(self):
        '''Cada elemento en una línea distinta empezando por el TOP de la pila''' 
        buffer = ""
        for item in self.items:
            buffer += f'{item}\n'
        return buffer

    def __add__(self, other: IntegerStack) -> IntegerStack:
        '''La segunda pila va "encima" de la primera'''
        ...        

    def __iter__(self) -> IntegerStackIterator:
        return IntegerStackIterator(self)


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        ...

    def __next__(self) -> int:
        ...
