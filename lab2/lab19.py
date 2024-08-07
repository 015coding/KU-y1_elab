age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
final1 = income * 0.2
final2 = 6000 - ((income - 30000)*0.12)
if age >= 15 and age <= 60 :
    if income <= 30000 :
        print(f"Your negative income tax is {final1:.2f} Baht.")
    elif income <= 79999 :
        print(f"Your negative income tax is {final2:.2f} Baht.")
    elif income >=80000 :
        print("Invalid income.")
else :
    print("Invalid age.")



