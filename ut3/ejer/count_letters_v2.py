sentence = 'boom'
counter = {}
for char in sentence:
    if char not in counter:
        counter[char] = 1
    else:
        counter[char] += 1
print(counter)
        