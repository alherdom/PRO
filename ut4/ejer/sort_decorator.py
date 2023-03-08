def order_type(type:bool=True):
    def sort_decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type:
                return sorted(func(*args, **kwargs))
            return sorted(func(*args, **kwargs), reverse=True)
        return wrapper
    return sort_decor

@order_type(True)
def sum_list(a: list, b: list) -> list:
    return a + b

a = [1,2,3,4]
b = [1,2,3,4]

print(sum_list(a,b))

