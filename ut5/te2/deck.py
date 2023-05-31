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
    
    def draw_random_card(self) -> Card:
        return self.deck.pop(random.randrange(len(self.deck)))
    
    def draw_first_card(self) -> Card:
        return self.deck.pop(0)
    
    def draw_last_card(self) -> Card:
        return self.deck.pop(-1)
    
    def show_random_card(self) -> str:
        print(self.draws_random_card())
    
    def show_first_card(self) -> str:
        print(self.draws_first_card())
        
    def show_last_card(self) -> str:
        print(self.draws_first_card())
    
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

# - Datos:
#   - 52 cartas ✔
# - Responsabilidades:
#   - Dar una carta aleatoria ✔
#   - Dar la carta de "arriba" ✔
#   - Dar la carta de "abajo" ✔
#   - Barajar ✔
#   - Ver una carta aleatoria ✔
#   - Ver la carta de "arriba" ✔
#   - Ver la carta de "abajo" ✔