x = int(input("x: "))
operator = str(input("Operator: "))
y = int(input("y: "))

if operator == "+" :
    print(x + y)
elif operator == "-" :
    print(x-y)
elif operator == '*' :
    print(x*y)
elif operator == "/" :
    a = x/y
    print(f"{a:.2f}")
elif operator =="%" :
    print(x%y)
else : 
    print("Unknown Operator")