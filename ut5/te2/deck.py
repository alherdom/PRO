from __future__ import annotations
from card import Card
import random
from typing import Generator, Iterable, MutableSequence

class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.GLYPHS.keys():
            for value in range(1,14):
                self.deck.append(Card(value, suit))
    
    def __getitem__(self, index: int) -> int:
        return self.deck[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.deck[index] = item

    def __len__(self) -> int:
        return len(self.deck)

    def __str__(self) -> str:
        return ','.join([str(item) for item in self.deck])

    def __iter__(self) -> DeckIterator:
        return DeckIterator(self)
    
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    
    def randint(a: int = -1, b: int = -1, /) -> int:
        '''Genera un valor aleatorio entre a y b (incluidos)'''
        if b == -1:
            a, b = 0, a
        if a < 0 or b < 0:
            raise ValueError('Args must be positive!')
        if a > b:
            raise ValueError('Upper bound must be greater than lower bound!')
        return random.randint(a, b)
    
class DeckIterator:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.counter = 0

    def __next__(self) -> int:
        if self.counter >= len(self.deck):
            raise StopIteration
        item = self.deck[self.counter]
        self.counter += 1
        return item

new_deck = Deck()
# for card in new_deck:
#     print(card)
# print(new_deck)
print(new_deck.shuffle())

# - Datos:
#   - 52 cartas
# - Responsabilidades:
#   - Dar una carta aleatoria
#   - Dar la carta de "arriba"
#   - Dar la carta de "abajo"
#   - Barajar
#   - Ver una carta aleatoria
#   - Ver la carta de "arriba"
#   - Ver la carta de "abajo"