# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
 
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#    15 - Love
#    30 - Love
#    30 - 15
#    30 - 30
#    40 - 30
#    Deuce
#    Ventaja P1
#    Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.   
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

def tennis_match(points:list) -> str:
    p1_points = 0
    p2_points = 0
    for point in points:
        if point == 'P1' and p1_points != 30:
            p1_points += 15
        elif point == 'P2' and p2_points != 30:
            p2_points += 15
        elif point == 'P1' and p1_points == 30:
            p1_points += 10
        elif point == 'P2' and p2_points == 30:
            p2_points += 10
        elif  
            