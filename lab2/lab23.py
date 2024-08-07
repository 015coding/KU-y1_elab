target = 72

num = int(input("Enter your guess (0 - 100): "))

while num != target :   
    
    if num < target and num >= 0:
        print("Sorry, your guess is too low, try again later.")
    elif num > target and num <= 100:
        print("Sorry, your guess is too high, try again later.")
    else:
        print("Sorry, out of range, try again later.")
    num = int(input("Enter your guess (0 - 100): "))
print("Congratulations, your guess is correct.")
        