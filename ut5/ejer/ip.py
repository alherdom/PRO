from __future__ import annotations

def load_ip(path: str = 'ip.dat') -> str:   
    return open(path).read()

class IP:
    
    def __init__(self, ip: str):
        self.ip = ip

    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE

    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object) -> bool:
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        return self.cmp_value == min(self.cmp_value, other.cmp_value)

    def __gt__(self, other: Card) -> bool:
        return self.cmp_value == max(self.cmp_value, other.cmp_value)

    def __add__(self, other: Card) -> Card:
        suit = self.suit if self.cmp_value > other.cmp_value else other.suit 
        value = Card.A_VALUE if self.cmp_value + other.cmp_value > Card.K_VALUE else self.value + other.value
        return Card(value, suit)

    def is_ace(self) -> bool:
        '''Indica si una carta es un AS'''
        return self.value == Card.A_VALUE

    @classmethod
    def get_available_suits(cls) -> str:
        '''Devuelve todos los palos como una cadena de texto'''
        return Card.CLUBS + Card.DIAMONDS + Card.HEARTS + Card.SPADES 

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        for gliphs in Card.GLYPHS[suit]:
            yield gliphs
        # return Card.GLYPHS[suit]


class InvalidIPError(Exception):
    def __init__(self, message: str = ""):
        self.message = "🃏 Invalid card"
        if message:
            self.message += f": {message}"
        super().__init__(message)

    def __str__(self):
        return self.message