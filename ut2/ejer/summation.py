# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.
LIMIT = 7
total_sum = 0
for num in range (1,LIMIT + 1):
    total_sum += num
    print(f'{num}{total_sum}')
print(total_sum)
    