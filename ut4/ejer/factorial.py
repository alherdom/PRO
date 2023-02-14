# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************



def factorial(n):  
    fact = n
    for i in range(1,n):
        fact *= (n - i)
        return fact
    
    

