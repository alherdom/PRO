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
print(output)
string_output = "".join(output)
print(string_output)
final_output = ""
for char in string_output:
    final_output += char
    position = string_output.find(char)
    if position % 2 != 0:
        final_output += "+"
    elif len(final_output) < 15:
        final_output += "⋅"
print(f"[{final_output}]={result}")
