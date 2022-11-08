# Complete the function which converts a binary number (given as a string)
# to a decimal number.

inp ="11111001000"
num = 0
inp = inp[::-1]
for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
print(num)