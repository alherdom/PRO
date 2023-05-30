from deck import Deck
from players import Player

class Dealer:
    def __init__(self, deck: Deck, players: list[Player]):
        self.deck = deck
        self.players = players
        self.community_cards = []
        
    def give_cards(self):
        for player in self.players:
            player.hole_cards = [self.deck.draw_random_card(), self.deck.draw_random_card()]
    
    def draw_community_cards(self):
        self.community_cards = [self.deck.draw_random_card() for _ in range(7)]

    def __str__(self):
        return ','.join(card for card in self.community_cards)
    
    def show_community_cards(self):
        print(self.community_cards)

new_dealer = Dealer(Deck(), Player('Alejandro', 'Antonio'))

# - Datos:
#   - Mazo
#   - Jugadores
# - Responsabilidades:
#   - Dar cartas a los jugadores
#   - Destapar cartas comunes