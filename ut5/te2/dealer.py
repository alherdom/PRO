from deck import Deck
from players import Player

class Dealer:
    def __init__(self, deck: Deck, players: list[Player]):
        self.deck = deck
        self.players = players
        self.community_cards = []
        
    def 
# - Datos:
#   - Mazo
#   - Jugadores
# - Responsabilidades:
#   - Dar cartas a los jugadores
#   - Destapar cartas comunes