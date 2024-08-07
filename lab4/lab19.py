def count_digits(number):
    count = len(str(number))
    return count

def get_last_digit(n):
   return n % 10

def get_distribution(number):
    strings = " "
    number = str(number)
    mods = 10
    num_len = len(number)
    number = int(number)
    for i in range(num_len):
        num_m = number % mods
        mods *= 10
        if i == num_len-1:
            strings += (f"{num_m//(10**(i))}x10^{i}")
        else :
            strings += (f"{num_m // (10 ** (i))}x10^{i} + ")
    return strings


num = input("Input number: ")
print(f"{num} ={get_distribution(num)} 1")