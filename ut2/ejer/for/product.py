number = 10
succesive = (
    1  # Acumulador de un producto que empieza en 1 por multplicacion por 0 igual 0.
)
for i in range(1, number + 1):
    succesive *= i**2
print(succesive, end=" ")
