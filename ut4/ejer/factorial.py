# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    if n < 0:
        fact = None
    else:
        fact = 1
        for i in range(n,0,-1):
            fact *= i    
    print(fact)

factorial(8)