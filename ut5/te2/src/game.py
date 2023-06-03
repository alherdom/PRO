from __future__ import annotations
from cards import Card, Deck, Hand
from roles import Dealer, Player

class Game:
    def __init__(self, number_players: int):
        pass
    
    def __repr__(self) -> str:
        return f'{self.players}{self.dealer}'

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