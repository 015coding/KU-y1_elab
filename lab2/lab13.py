one = str(input("Is Bulotelli injured?(y/n) "))
if one == "y" :
    print("Not available")
else :
    two = str(input("Is Bulotelli late for the training?(y/n) "))
    if two == "y" :
        three = str(input("Did Bulotelli perform well in training?(y/n) "))
        if three == "y" :
            print("Substitute")
        else :
            print("Not selected")
    else :
        print("Starter")
