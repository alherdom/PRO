from __future__ import annotations
from cards import Card, Deck, Hand
from roles import Dealer, Player

def get_winner(
    players: list[Player],
    common_cards: list[Card],
    private_cards: list[list[Card]],
) -> tuple[Player | None, Hand]:
    player = Player('Player 1')
    hand = Hand([Card('9♠'), Card('A♠'), Card('6♣'), Card('10♠'), Card('6♠')])
    return player, hand
    
class Game:
    def __init__(self, number_players: int):
        self.deck = Deck()
        self.dealer = Dealer
        self.number_players = number_players
        self.players = []
    
    @property    
    def create_players(self):
        self.players = [Player(str(i)) for i in range(1,self.number_players + 1)]
    
    @property
    def create_dealer(self):
        self.dealer = Dealer(self.deck, self.players)
        
    def show_players(self) -> str:
        return f'{self.players}'
        
    def show_dealer(self):
        return f'{self.dealer}'
    
    def deal_cards_to_players(self):
        self.dealer.draw_random_cards()
        
    def deal_community_cards(self):
        self.dealer.draw_community_cards()
    
    # if __name__ == '__main__':

        
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

game1 = Game(1)
game1.create_players
game1.create_dealer
game1.deal_cards_to_players()
game1.deal_community_cards()
# print(game1.show_dealer())
print(game1.players[0])
print(game1.players[0].is_royal_flush())