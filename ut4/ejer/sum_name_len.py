names = ["ana", "pepa", "maria"]

def pnames(names:list,size=0):
    if n >= 0:
        size += len(names[0])
        return pnames(names[1:],size)

print(pnames(names))
    





# def countdown(n):
#     print(n)
#     if n > 0:
#         countdown(n -1)
# countdown(5)