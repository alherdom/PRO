from __future__ import annotations
from deck import Deck
from players import Player
from dealer import Dealer
from hand import Hand

class Game:
    def __init__(self, number_players: int):
        self.number_players = number_players
        self.deck = Deck()
        self.players = [Player(f'Player{i}') for i in range(number_players)]
        self.dealer = Dealer(self.deck, self.players)
    
    def start_game(self):
        Dealer.give_cards(self)
        

# - Datos:
#   - Deck ✔
#   - Players ✔
#   - Dealer ✔
# - Responsabilidades:
#   - Crear un mazo ✔
#   - Crear los jugadores ✔
#   - Crear el dealer ✔
#   - Comenzar la partida (repartir cartas, buscar mejor combinación)
#   - Finalizar la partida (mostrar el ganador y su mano)