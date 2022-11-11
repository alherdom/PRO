# Dados dos vectores (listas) de la misma dimensión, utilice la función zip() para calcular su producto escalar.
# Ejemplo
# Entrada:
# v1 = [4, 3, 8, 1]
# v2 = [9, 2, 7, 3]
# Salida: 101
# 𝑣1×𝑣2=[4⋅9+3⋅2+8⋅7+1⋅3]=101

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
result = 0
output = []
for value1, value2 in zip(v1, v2):
    result += value1 * value2
    output += str(value1) + str(value2)
print(result)
# output_sep = "-".join([output])
print(output)
