from __future__ import annotations
from helpers import randint, shuffle, combinations

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
#   - Glifo de la carta ✔
# - Responsabilidades:
#   - Saber si una carta es menor que otra ✔
#   - Representar la carta ✔

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
        return ','.join([str(item) for item in self])

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
        return f'{self.draws_random_card()}'
    
    def show_top_card(self) -> str:
        return f'{self.draws_top_card()}'
        
    def show_bottom_card(self) -> str:
        return f'{self.draws_bottom_card()}'
    
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
    def __init__(self) -> None:
        pass
    
    def __contains__(a, b) -> bool:
        pass
    
    def __str__(self) -> str:
        return ','.join([str(item) for item in self])
    
class HandIterator:
    def __init__(self, hand: Hand):
        self.cards = hand
        self.counter = 0

    def __next__(self) -> int:
        if self.counter >= len(self.deck):
            raise StopIteration
        item = self.deck[self.counter]
        self.counter += 1
        return item
    
# 1º Escalera Real: 5 cartas seguidas del mismo palo desde el 10 al As.
# 4 posibles escaleras reales (por palo)
# tener mismo palo, y consecutivas desde value 10 al 14 (24)
royal_flush_clubs = ('♣', '🃚🃛🃝🃞🃑')
royal_flush_diamonds = ('◆', '🃊🃋🃍🃎🃁')
royal_flush_hearts = ('❤', '🂺🂻🂽🂾🂱')
royal_flush_spades = ('♠', '🂪🂫🂭🂮🂡')

# 2º Escalera color: 5 cartas consecutivas del mismo color.
# 5 values de menos a mas, consecutivos, y del mismo suit

# 3º Poker: 4 cartas iguales.
# 4 values iguales

# 4º Full: 3 cartas iguales más otras 2 iguales. Es decir, un trio y una pareja.
# En caso de empate, gana el que tiene el trio más alto.
# 3 values iguales, y 2 values iguales, value de 3 más alto gana

# 5º Color: 5 cartas del mismo palo.
# mismo suit en la mano

# 6º Escalera: 5 cartas consecutivas que no son del mismo palo.
# 5 values de menos a mas, consecutivos, y de distinto suit

# 7º Trío: 3 cartas iguales.
# sólo 3 values iguales

# 8º Doble pareja: Dos parejas de cartas iguales.
# dos 2 values iguales

# 9º Pareja: Una pareja de cartas iguales.
# uno 2 values iguales

# 10º Carta más alta: Si en el transcurso de la partida ningún jugador consigue formar alguna de las combinaciones presentadas más arriba,
# el ganador de la partida será el que tenga la carta más fuerte, siendo el As la mejor en estos casos. Es también la carta más fuerte 
# la que desempata dos combinaciones idénticas.
# value más alto

# - Datos:
#   - 5 cartas
# - Responsabilidades:
#   - Descubrir la categoría de la mano
#   - Asignar una puntuación a la categoría
#   - Saber si una mano es mejor que otra (ranking)