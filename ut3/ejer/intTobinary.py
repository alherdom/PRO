# Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.

number = 25
output = []
result = 0
while number >= 1:
    output.append(str(number % 2))
    number //= 2
print(output)
to_bin = list(reversed(output))
print(to_bin)
