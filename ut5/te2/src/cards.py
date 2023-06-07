from __future__ import annotations
from helpers import randint, shuffle, combinations
import re

class Card:
    GLYPHS = {
        '♣':'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞',
        '◆':'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎',
        '❤':'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾',
        '♠':'🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'
        }
    
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    
    def __init__(self, value_suit: str):
        regex = r'\+?(?P<value>\d{1,2}|[AJQK])(?P<suit>.*)'
        m = re.search(regex, value_suit)
        value, suit = m.groups()
        self.value = int(value)
        self.suit = suit

    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE

    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE

    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card) -> bool:
        return self.cmp_value == other.cmp_value and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        return self.cmp_value == min(self.cmp_value, other.cmp_value)

class InvalidCardError(Exception):
    def __init__(self, message: str = ""):
        self.message = "🃏 Invalid card"
        if message:
            self.message += f": {message}"
        super().__init__(message)

# - Datos:
#   - Número de la carta ✔
#   - Palo de la carta ✔
# - Responsabilidades:
#   - Saber si una carta es menor que otra ✔
#   - Representar la carta ✔

class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.GLYPHS.keys():
            for value in range(1,14):
                self.deck.append(Card(str(value) + suit))
        shuffle(self.deck)
    
    def __getitem__(self, index: int) -> int:
        return self.deck[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.deck[index] = item

    def __len__(self) -> int:
        return len(self.deck)

    def __iter__(self) -> DeckIterator:
        return DeckIterator(self)
    
    def shuffle_deck(self) -> None:
        shuffle(self.deck)
    
    def draw_random_card(self) -> Card:
        return self.deck.pop(randint(len(self.deck)-1))
    
    def draw_top_card(self) -> Card:
        return self.deck.pop(0)
    
    def draw_bottom_card(self) -> Card:
        return self.deck.pop(-1)
    
    def show_random_card(self) -> str:
        return f'{self.draw_random_card()}'
    
    def show_top_card(self) -> str:
        return f'{self.draw_top_card()}'
        
    def show_bottom_card(self) -> str:
        return f'{self.draw_bottom_card()}'
    
    def __repr__(self) -> str:
        return ','.join(str(card) for card in self.deck)
    
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

class Hand:
    def __init__(self, player_cards = list[Card]):
        self.player_cards = player_cards
        
    def __contains__(a, b) -> bool:
        pass
  
# - Datos:
#   - 5 cartas
# - Responsabilidades:
#   - Descubrir la categoría de la mano
#   - Asignar una puntuación a la categoría
#   - Saber si una mano es mejor que otra (ranking)