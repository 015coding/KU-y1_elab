
for i in range (3):
    enter = str(input("Please enter password: "))
    if enter == "Python is fun":
        print("Correct password")
        print("Access granted")
        break
    else :
        print(f"Incorrect password, attempt #{i+1}")
        print("Access not allowed")
else :
    print("Maximum attempts exceeded")


