def counter():
    count = 0
    def function():
        nonlocal count
        count += 1
        return count
    return function

print(counter())