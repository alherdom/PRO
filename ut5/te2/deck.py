from __future__ import annotations
from card import Card

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

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return ','.join([str(item) for item in self.deck])

    def __iter__(self) -> DeckIterator:
        return DeckIterator(self)


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
for card in new_deck:
    print(card)
print(new_deck)