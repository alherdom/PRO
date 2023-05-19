from __future__ import annotations


class Card:
    GLYPHS = {'♣':'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞', '◆':'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎','❤':'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾','♠':'🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'}
    CLUBS = '♣'
    DIAMONDS = '◆'
    HEARTS = '❤'
    SPADES = '♠'
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    
    def __init__(self, value: int | str, suit: str = ''):
        # if isinstance(value, str) and value not in Card.SYMBOLS:
        #     raise InvalidCardError(f"{repr(value)} is not a supported symbol")
        # if value > Card.K_VALUE or value < Card.A_VALUE:
        #     raise InvalidCardError(f"{repr(value)} is not a supported value")
        # if suit not in Card.GLYPHS.keys():
        #     raise InvalidCardError(f"{repr(suit)} is not a supported suit")
        if isinstance(value, str) and suit == None:
            for suit, glyphs in Card.GLYPHS.items():
                for i, glyph in enumerate (glyphs):
                    if value == glyph:
                        self.value = i + 1
                        self.suit = suit 
        self.value = value
        self.suit = suit

    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE

    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][int(self.value) - 1]

    def __eq__(self, other: Card | object) -> bool:
        return self.value == other.value

    def __lt__(self, other: Card) -> bool:
        return self.cmp_value == min(self.cmp_value, other.cmp_value)

    def __gt__(self, other: Card) -> bool:
        return self.cmp_value == max(self.cmp_value, other.cmp_value)

    def __add__(self, other: Card) -> Card:
        suit = self.suit if self.cmp_value > other.cmp_value else other.suit 
        value = Card.A_VALUE if self.cmp_value + other.cmp_value > Card.K_VALUE else self.value + other.value
        return Card(value, suit)

    @staticmethod
    def build_deck():
        for suit in GLYPHS.keys():
            for value in GLYPHS[suit]:
                yield Card(value, suit)

    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE

    @classmethod
    def get_available_suits(cls) -> str:
        return cls.GLYPHS.keys()

    # DECK
    @classmethod
    def get_cards_by_suit(cls, suit: str):
        return GLYPHS[suit]

class InvalidCardError(Exception):

    def __init__(self, message: str = ""):
        self.message = "🃏 Invalid card"
        if message:
            self.message += f": {message}"
        super().__init__(message)
        
        
card2 = Card('🂦')
print(card2)