number = float(input("Enter your guess (0 - 100): "))
target = 72

if number  >= 0 and number <= 100 :
    if number > target :
        print("Sorry, your guess is too high, try again later.")
    elif number < target :
        print("Sorry, your guess is too low, try again later.")
    elif number == target :
        print("Congratulations, your guess is correct.")
else :
    print("Sorry, out of range, try again later.")

    
