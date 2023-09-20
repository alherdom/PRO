import sys

number = sys.argv[1]
product_size = int(sys.argv[2])

def mult(numbers: list[int])->int:
    total = 1
    for i in numbers:
        total *= i
    return total

def calc_max_product(current_number: str, product_size:int, max_n: int = 0):
    if len(current_number) < product_size:
        return max_n
    product = mult([int(i) for i in current_number[:product_size]])
    if product > max_n:
        max_n = product
    return calc_max_product(current_number[1:], product_size,max_n)

def max_product(number:str, product_size:int) -> int:
    if product_size > len(number) or product_size <= 0 or not number.isnumeric():
        raise ValueError("Invalid input arguments!")
    return calc_max_product(number, product_size)
    
print(max_product(number,product_size))