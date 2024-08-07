p = int(input("Input p: "))


def fraction(p):
    return (2*(p**4)) - (5*(p**3)) - (24*(p**2)) - (7*p) + 10

print("Fraction = %d" % fraction(p))