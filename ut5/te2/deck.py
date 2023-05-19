import card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in card.Card.GLYPHS.keys():
            for value in range(1,14):
                self.cards.append(card.Card(value, suit))
                
        # self.cards = []
        # for suit in Card.GLYPHS.keys():
        #     self.cards += [card for card in Card.GLYPHS[suit]] 
    
    def hola(self):
        return self.cards

#     def __iter__(self) -> CardIterator:
#         return CardIterator(self)


# class CardIterator:
#     def __init__(self, deck: Deck):
#         self.deck = deck
#         self.counter = 0

#     def __next__(self) -> int:
#         if self.counter >= len(self.deck):
#             raise StopIteration
#         item = self.queue.items[self.counter]
#         self.counter += 1
#         return item
    
#     for byte in self.host_bip_segments:
#             byte_length = len(byte)
#             if byte.count(1) == byte_length:
#                 raise StopIteration
#             if byte.count(0) != byte_length:
#                 new_ip = self.host.addr_bmask + "".join(str(bit) for bit in byte)
#                 return Host.from_bip(new_ip, self.host.mask)

new_deck = Deck()
print(new_deck.hola())
