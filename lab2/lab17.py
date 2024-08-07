Type = str(input("Enter your buffet choice: "))


if Type == "Japanese" :
    today = str(input("Is today Wednesday (yes/no)? "))
    if today == "yes" :
        print("Your payment is 850.00 Baht.")
    else :
        print("Your payment is 1000.00 Baht.")
elif Type == "Korean" :
    today = str(input("Is today Wednesday (yes/no)? "))
    if today == "yes" :
        print("Your payment is 1275.00 Baht.")
    else :
        print("Your payment is 1500.00 Baht.")    
else :
    print(f"Sorry, there is no {Type} buffet.")



