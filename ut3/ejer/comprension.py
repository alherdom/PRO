# Utilizando listas por comprensión, cree una lista que contenga el resultado de aplicar la función 𝑓(𝑥)=3𝑥+2 para 𝑥∈[0,20).
# Salida esperada: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59].
X_UPPER_LIMIT = 20
a = 3
b = 2
function = [a * x + b for x in range(X_UPPER_LIMIT)]
print(function)
