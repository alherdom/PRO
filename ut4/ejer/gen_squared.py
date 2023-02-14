def gen_squared(n):
    gen_list = []
    for i in range(0,n+1):
        number = i**2
        gen_list.append(number)
    return gen_list
print(gen_squared(100))