# ******************
# FIBONACCI ITERABLE
# ******************

# num_ini = 0
# num_ulti = 1
# num_result = 0
# for _ in range(98):
#     num_result = num_ini + num_ulti
#     num_ini = num_ulti
#     num_ulti = num_result


class Fibonacci:
        def __init__(self, n: int):
            self.limit = n
            self.pointer = 0
            self.values = []
        
        def __iter__(self):
            return self

        def __next__(self):
            
            if self.pointer >= self.limit:
                raise StopIteration
            
            self.pointer += 1
            
            return ...

# def run():