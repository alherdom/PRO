# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
