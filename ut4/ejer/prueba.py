items = (1,2,2,1,3,2,4)
value = 2
ini = 0
# count = 0
# for i in items:
#     if value == i:
#         count +=1

count = [sum(i for i in items if i == value)/value]
print(count)