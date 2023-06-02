from __future__ import annotations
from ut5.te2.src.cards import Deck

class Dealer:
    def __init__(self, deck: Deck, players: list[Player]):
        self.deck = deck
        self.players = players
        self.community_cards = []
        
    def give_cards(self):
        for player in self.players:
            player.hole_cards = [self.deck.draw_random_card(), self.deck.draw_random_card()]
    
    def draw_community_cards(self):
        self.community_cards = [self.deck.draw_random_card() for _ in range(5)]
        
    def __str__(self):
        return ','.join(card for card in self.community_cards)
    
    def show_community_cards(self):
        print(self.community_cards)

# - Datos:
#   - Mazo ✔
#   - Jugadores ✔ 
# - Responsabilidades:
#   - Dar cartas a los jugadores ✔
#   - Destapar cartas comunes ✔

from typing import Generator, Iterable, MutableSequence

def combinations(values: Iterable, *, n: int = 5) -> Generator:
        '''Genera todas las combinaciones de "values" de tamaño "n"'''
        def combinations_helper(items, k=0, h=0):
            if k == n:
                yield tuple(items)
            else:
                for i in range(h, len(values)):
                    items[k] = values[i]
                    yield from combinations_helper(items, k + 1, i + 1)
        return combinations_helper([None] * n)

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hole_cards = []
        self.community_cards = []
       
    def find_best_hand(self):
        pass
        
# 1º Escalera Real: 5 cartas seguidas del mismo palo desde el 10 al As.
# 2º Escalera color: 5 cartas consecutivas del mismo color.
# 3º Poker: 4 cartas iguales.
# 4º Full: 3 cartas iguales más otras 2 iguales. Es decir, un trio y una pareja. En caso de empate, gana el que tiene el trio más alto.
# 5º Color: 5 cartas del mismo palo.
# 6º Escalera: 5 cartas consecutivas que no son del mismo palo.
# 7º Trío: 3 cartas iguales.
# 8º Doble pareja: Dos parejas de cartas iguales.
# 9º Pareja: Una pareja de cartas iguales.
# 10º Carta más alta: Si en el transcurso de la partida ningún jugador consigue formar alguna de las combinaciones presentadas más arriba,
# el ganador de la partida será el que tenga la carta más fuerte, siendo el As la mejor en estos casos. Es también la carta más fuerte 
# la que desempata dos combinaciones idénticas.

# - Datos:
#   - Nombre ✔ 
#   - 2 cartas propias ✔
#   - 5 cartas comunes ✔
# - Responsabilidades:
#   - Encontrar su mejor combinación de cartas