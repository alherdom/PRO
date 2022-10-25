# Imprima los 100 primeros números de la sucesión de Fibonacci: 0,1,1,2,3,5,8,13,21,34,55,89,…
num_ini = 0
num_ulti = 1
num_result = 0
for _ in range(98):
    num_result = num_ini + num_ulti
    num_ini = num_ulti
    num_ulti = num_result
    print(num_result)
print(f"{num_ini} + {num_ulti} = {num_result}")
