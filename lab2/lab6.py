buying = float(input("Enter buying amount: "))

if buying < 3000 and buying >= 1000 :
    final1 = buying*0.9
    print(f"Amount due after discount is {final1:.2f} baht.")
elif buying >= 3000 :
    final2 = buying*0.85
    print(f"Amount due after discount is {final2:.2f} baht.")
elif buying < 1000 :
    print(f"Amount due after discount is {buying:.2f} baht.")
