path = "cards.dat"

with open(path) as f:
    glyphs = {}
    suits = []
    cards = []
    for line in f:
        suits.append(line[0])
        cards.append(line[2:].strip().replace(",",""))
    for suit, card in zip(suits, cards):
        glyphs[suit] = card
    print(glyphs)
    
    
cards2 = glyphs["♣"]

print(cards2[0])