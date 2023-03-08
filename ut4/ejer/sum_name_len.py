names = ["ana", "pepa", "maria"]

def s_names(names:list, size=0):
    if len(names) == 1:
        size += len(names[0])
        return size
    size += len(names[0])
    return s_names(names[1:], size) 
    
print(s_names(names))
    
# def countdown(n):
#     print(n)
#     if n > 0:
#         countdown(n -1)
# countdown(10)