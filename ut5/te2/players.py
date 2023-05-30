from __future__ import annotations

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hole_cards = []
        self.community_cards = []
    
    def __str__(self) -> str:
        return f'{self.name}, {self.hole_cards}, {self.community_cards}'

# - Datos:
#   - Nombre
#   - 2 cartas propias
#   - 5 cartas comunes
# - Responsabilidades:
#   - Encontrar su mejor combinación de cartas