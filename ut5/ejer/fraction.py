class Fraction:
    def __init__(self, num: int, den: int):
        if not isinstance(num, int) or not isinstance(den, int):
            raise ValueError("Numerador y denominador deben de ser de tipo entero.")
        gcd = self.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Algoritmo de Euclides para el cálculo del Máximo Común Divisor."""
        while b > 0:
            a, b = b, a % b
        return a

    def __str__(self) -> str:
        return f"\n{self.num}\n__\n\n{self.den}\n"

    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = (self.num * other.den) - (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __floordiv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den
    
    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

fraction1 = Fraction(25, 30)
fraction2 = Fraction(40, 45)

fraction3 = fraction1 + fraction2
print(fraction3)

fraction4 = fraction1 - fraction2
print(fraction4)

fraction5 = fraction1 * fraction2
print(fraction5)

fraction6 = fraction1 // fraction2
print(fraction6)
