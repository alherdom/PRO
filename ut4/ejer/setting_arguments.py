# Fijando argumentos posicionales y nominales.
# Si mezclamos las dos estrategias anteriores podemos forzar a que una función reciba argumentos
# de un modo concreto.
# Continuando con el ejemplo anterior, podríamos hacer lo siguiente:

# IZQUIERDA DE LA / = SOLO POSICIONALES    DERECHA DEL * = SOLO NOMINALES
def sum_power(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b

sum_power(3, 4, power=True)  # Único modo posible de llamada

# CUANDO SE EMPLEAN DE MANERA INDEPENDIENTE, EL LADO "NO FIJADO" SE ESTABLECE COMO SIEMPRE, 
# POSICIONALES-NOMINALES.