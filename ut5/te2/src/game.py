from __future__ import annotations
from cards import Card, Deck, Hand
from roles import Dealer, Player

class Game:
    def __init__(self, number_players: int):
        self.number_players = number_players
        self.deck = Deck()
        self.players = [Player(f'Player{i}') for i in range(number_players)]
        self.dealer = Dealer(self.deck, self.players)
    
    def start_game(self):
        Dealer.give_cards(self)
    
    def __str__(self):
        print(self)
    
    def show_players(self):
        print(self.players)
    
    def get_winner(self):
        pass
        

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

new_game = Game(3)

new_game.start_game()

print(new_game.show_players())