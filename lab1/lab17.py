P = float(input("Input principal amount (P): "))
r = float(input("Input annual nominal interest rate (r): "))
n = float(input("Input # of times the interest is compounded per year (n): "))
t = float(input("Input # of years (t): "))

final = P*((1+(r/n))**(n*t))

print(f"Final amount: {final:.2f}")