from __future__ import annotations

class Hand:
    def __init__(self) -> None:
        pass


# 1º Escalera Real: 5 cartas seguidas del mismo palo desde el 10 al As.
# 4 posibles escaleras reales (por palo)
# tener mismo palo, y consecutivas desde value 10 al 14 (24)
royal_flush_clubs = ('♣', '🃚🃛🃝🃞🃑')
royal_flush_diamonds = ('◆', '🃊🃋🃍🃎🃁')
royal_flush_hearts = ('❤', '🂺🂻🂽🂾🂱')
royal_flush_spades = ('♠', '🂪🂫🂭🂮🂡')

# 2º Escalera color: 5 cartas consecutivas del mismo color.
# 5 values de menos a mas, consecutivos, y del mismo suit

# 3º Poker: 4 cartas iguales.
# 4 values iguales

# 4º Full: 3 cartas iguales más otras 2 iguales. Es decir, un trio y una pareja.
# En caso de empate, gana el que tiene el trio más alto.
# 3 values iguales, y 2 values iguales, value de 3 más alto gana

# 5º Color: 5 cartas del mismo palo.
# mismo suit en la mano

# 6º Escalera: 5 cartas consecutivas que no son del mismo palo.
# 5 values de menos a mas, consecutivos, y de distinto suit

# 7º Trío: 3 cartas iguales.
# sólo 3 values iguales

# 8º Doble pareja: Dos parejas de cartas iguales.
# dos 2 values iguales

# 9º Pareja: Una pareja de cartas iguales.
# uno 2 values iguales

# 10º Carta más alta: Si en el transcurso de la partida ningún jugador consigue formar alguna de las combinaciones presentadas más arriba,
# el ganador de la partida será el que tenga la carta más fuerte, siendo el As la mejor en estos casos. Es también la carta más fuerte 
# la que desempata dos combinaciones idénticas.
# value más alto

# - Datos:
#   - 5 cartas
# - Responsabilidades:
#   - Descubrir la categoría de la mano
#   - Asignar una puntuación a la categoría
#   - Saber si una mano es mejor que otra (ranking)