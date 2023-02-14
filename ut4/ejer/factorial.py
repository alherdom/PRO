# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    fact = n
    if n == 0:
        fact = 1
    elif n < 0:
        fact = None
    else:
        for i in range(1,n):
            fact *= (n - i)    
    return fact

