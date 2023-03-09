def order_output(ascending: bool = True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            return sorted(output, reverse = not ascending)
        return wrapper
    return decorator

@order_output()
def sum_list(a: list, b: list) -> list:
    return a + b

a = [1,2,3,4]
b = [1,2,3,4]

print(sum_list(a,b))

