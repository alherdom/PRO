from __future__ import annotations

class Card:
    GLYPHS = {'♣':'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞', '◆':'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎','❤':'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾','♠':'🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'}
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13

    def __init__(self, value: int | str, suit: str = ''):
        if suit:
            if isinstance(value, str) and value not in Card.SYMBOLS:
                raise InvalidCardError(f"{repr(value)} is not a supported symbol")
            if isinstance(value, int) and not (Card.A_VALUE <= value <= Card.K_VALUE):
                raise InvalidCardError(f"{repr(value)} is not a supported value")
            if suit not in Card.GLYPHS.keys():
                raise InvalidCardError(f"{repr(suit)} is not a supported suit")
        elif isinstance(value, str):
            for suit, glyphs in Card.GLYPHS.items():
                if value in glyphs:
                    self.value = glyphs.index(value) + 1
                    self.suit = suit
                    return
            raise InvalidCardError(f"{repr(value)} is not a supported symbol")
        else:
            self.value = int(value)
            self.suit = suit

    def is_ace(self) -> bool:
        return self.value == Card.A_VALUE
    
    @property
    def cmp_value(self) -> int:
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE

    def __repr__(self) -> str:
        return Card.GLYPHS[self.suit][int(self.value) - 1]

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
#   - Glifo de la carta ✔
# - Responsabilidades:
#   - Saber si una carta es menor que otra ✔
#   - Representar la carta ✔