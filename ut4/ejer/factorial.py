# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    for i in range(1,n+1):
        fact = n 
        fact *= n * n - i
        return fact
    
    

