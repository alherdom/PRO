from __future__ import annotations


def load_card_glyphs(path: str = 'cards.dat') -> dict[str, str]:
    '''Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador'''
    
    with open(path) as f:
        glyphs = {}
        suits = []
        cards = []
        for line in f:
            suits.append(line[0])
            cards.append(line[2:].strip().replace(",",""))
        for suit, card in zip(suits, cards):
            glyphs[suit] = card
        return glyphs            
    


class Card:
    CLUBS = '♣'
    DIAMONDS = '◆'
    HEARTS = '❤'
    SPADES = '♠'
    SUITS = CLUBS+DIAMONDS+HEARTS+SPADES 
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        '''Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)'''
        if isinstance(value, str):
            value = int(value)
        if suit not in Card.SUITS :
            raise InvalidCardError(f"🃏 Invalid card: {repr(suit)} is not a supported suit")
        
        self.value = value if value >= 1 and value <= 13 else None
        self.suit = suit

    @property
    def cmp_value(self) -> int:
        '''Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS.'''
        return self.value

    def __repr__(self):
        '''Devuelve el glifo de la carta'''
        cards = Card.GLYPHS[self.suit]
        return cards[self.value - 1]

    def __eq__(self, other: Card | object) -> bool:
        '''Indica si dos cartas son iguales'''
        return True if self.value == other.value and self.suit == other.suit else False

    def __lt__(self, other: Card):
        '''Indica si una carta vale menos que otra'''
        if self.is_ace() and not other.is_ace():
            return False
        if other.is_ace() and not self.is_ace():
            return True
        return True if self.value == min(self.value, other.value) else False
        

    def __gt__(self, other: Card):
        '''Indica si una carta vale más que otra'''
        if self.is_ace() and not other.is_ace():
            return True
        if other.is_ace() and not self.is_ace():
            return False
        return True if self.value == max(self.value, other.value) else False
        

    def __add__(self, other: Card) -> Card:
        '''Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS.'''
        suit = self.suit if self.value > other.value else other.suit 
        value = 1 if self.value + other.value > 13 else self.value + other.value
        if self.is_ace() and not other.is_ace():
            suit = self.suit
        if other.is_ace() and not self.is_ace():
            suit = self.suit
        return Card(value, suit)

    def is_ace(self) -> bool:
        '''Indica si una carta es un AS'''
        return True if self.value == 1 else False

    @classmethod
    def get_available_suits(cls) -> str:
        '''Devuelve todos los palos como una cadena de texto'''
        return Card.SUITS

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        '''Función generadora que devuelve los glifos de las cartas por su palo'''
        return Card.GLYPHS[suit]


class InvalidCardError(Exception):
    '''Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea'''
    def __init__(self,*, message: str = "🃏 Invalid card"):
        self.message = message

    def __str__(self):
        return self.message
    
    # 🃏 Invalid card: {repr(suit)} is not a supported suit
    #     - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
    #     elevar una excepción de tipo InvalidCardError() con el mensaje:
    #     🃏 Invalid card: {repr(value)} is not a supported value
    #     - Si el value(como string) no es válido hay que elevar una excepción de tipo
    #     🃏 Invalid card: {repr(value)} is not a supported symbol