# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    def divisors(n:int) -> list:
        limit = (n//2) + 1
        divisors = [i for i in range(1,limit) if n % i == 0]
        return divisors
    if n == sum(divisors(n)):
        return True
    return False


