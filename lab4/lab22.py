numbers = input("Enter list of tuple: ").split()
digits = []

for number in numbers:
    a = tuple(int(char) for char in number)
    digits.append(a)
print(f"Input list: {digits}")
print(f"Output list: {sorted(digits,key=lambda x: x[-1])}")