def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

m3 = make_multiplier_of(3) 

print(m3(5))