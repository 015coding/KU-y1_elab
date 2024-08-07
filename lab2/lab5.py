number = float(input("Enter your guess (0 - 100): "))
target = 72

if number  >= 0 and number <= 100 :
    
    if number == target :
        print("Congratulations, your guess is correct.")
    else :
        print("Sorry, your guess is wrong, try again later.")
else :
    print("Sorry, out of range, try again later.")
    