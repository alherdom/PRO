BIN_N = '1101'
bin_size = len(BIN_N)
result = 0
for i in range (bin_size):
    digit = int(BIN_N[i])
    exponent = bin_size - i - 1
    partial_result = digit * 2**exponent
    result += partial_result
    print(f'({digit}{exponent}² = {partial_result})')
print(result)