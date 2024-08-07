def count_digits(number):
    if number < 0:
        number *= -1
    count = len(str(number))
    while True:
        break
    return count
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")