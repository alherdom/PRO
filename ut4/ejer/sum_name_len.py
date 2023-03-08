names = ["ana", "pepa", "maria"]

def pnames(names:list,n:int):
    if n >= 0:
        name = names[n]
        print(name)
        return pnames(names,n-1)

print(pnames(names,2))
    





# def countdown(n):
#     print(n)
#     if n > 0:
#         countdown(n -1)
# countdown(5)