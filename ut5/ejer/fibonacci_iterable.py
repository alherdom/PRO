# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
        def __init__(self, n: int):
            self.limit = n
            self.pointer = 0
            self.first_value = -1
            self.second_value = 1
                
        def __str__(self):
            return f'Fibo list is: {self.next_value}'
        
        def __iter__(self):
            return self

        def __next__(self):
            if self.pointer >= self.limit:
                raise StopIteration
            self.next_value = self.first_value + self.second_value
            self.first_value = self.second_value
            self.second_value = self.next_value
            self.pointer += 1
            return self.next_value

# fibo1 = Fibonacci(10)
# print(fibo1)
# print(next(fibo1))
# print(next(fibo1))
# print(next(fibo1))
# print(next(fibo1))
# print(next(fibo1))

def run(n):
    return list(Fibonacci(n))
