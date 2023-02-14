# def gen_squared(n):
#     gen_list = []
#     for i in range(0,n+1):
#         number = i**2
#         gen_list.append(number)
#     return gen_list
# print(gen_squared(100))

def gen_squared(n=100):
    for i in range(n):
        yield i ** 2
        
for i in gen_squared():
    print(i)
    