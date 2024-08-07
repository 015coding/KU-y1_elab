minutes = int(input("Minutes before due: "))
Temp = float(input("Temperature: "))
raining = str(input("Is it raining (y/n)? "))

day = minutes // 1440
date = minutes - (day *1440)

if date >= 720 :
    day +=1


if day < 2 :
    print(f">>> {day} days before due.")
    print(">>> I will do the assignment.")
elif day >=2 and day <= 5 :
    if Temp > 40 :
        print(f">>> {day} days before due.")
        print(">>> I will not do the assignment.")
    elif Temp > 25 and raining == "y" or raining == "Y":        
        print(f">>> {day} days before due.")
        print(">>> I will not do the assignment.")
    else:
        print(f">>> {day} days before due.")
        print(">>> I will do the assignment.")
    
elif day > 5 :
    print(f">>> {day} days before due.")
    print(">>> I will not do the assignment.")



