# ******************
# FIBONACCI ITERABLE
# ******************

class Fibonacci:
        def __init__(self, n: int):
            self.limit = n
            self.pointer = 0
            self.values = [0]
            initial_value = -1
            last_value = 1
            next_value = 0
            while len(self.values) < self.limit + 1:
                next_value = initial_value + last_value
                initial_value = last_value
                last_value = next_value
                self.values.append(next_value)
        
        def __iter__(self):
            return self

        def __next__(self):
            if self.pointer >= self.limit:
                raise StopIteration
            self.pointer += 1
            return self.values[self.pointer]

def run(n):
    return list(Fibonacci(n))