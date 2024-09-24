class Fraction:
    def __init__(self, int1, int2):
        def find_fac(int1, int2):
            x = max(int1, int2)
            if int1 == 0:
                self.int2 = 1
                pass

            while int1 % x != 0 or int2 % x != 0:
                x -= 1
            return x
        x = find_fac(int1, int2)
        self.int1 = int1 / x
        self.int2 = int2 / x
        self.a = find_fac(int1, int2)

    def evaluate(self):
        return self.int1 / self.int2

    def add(self, int_n):
        return Fraction((self.int2*int_n) + self.int1, self.int2)

    def __add__(self, other):
        #if self.int2 == other.int2:
         #   return self.int1 + other.int1, self.int2
        #else:
        return Fraction(self.int1 * other.int2 + self.int2 * other.int1, self.int2*other.int2)
    def multiply(self, int_n):
        return Fraction(self.int1 * int_n, self.int2)

    def __mul__(self, other):
        return Fraction(self.int1 * other.int1, self.int2 * other.int2)
    def __toString__(self):
        return Fraction(self.int1, self.int2)
    def __str__(self):
        return f"{self.int1:.0f} / {self.int2:.0f}"

print(Fraction(22, 7).multiply(7).multiply(7).multiply(7).multiply(7))
print((Fraction(1,2) + Fraction(3,4)).multiply(0))
print((Fraction(22,14) * Fraction(2, 4)).add(1))