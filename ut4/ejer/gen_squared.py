# *******************
# GENERANDO CUADRADOS
# *******************

def gen_sq(n):
    gen_sq = (i**2 for i in range(n))
    squared = list(gen_sq)
    return squared
    
