strings = str(input("Enter a string: "))
num = int(input("Enter arrow's size (greater than 0): "))


if num > 0 :
    if num%2==1 :
        num = (num // 2) +1
        for i in range(num):
            print(' ' * i + strings)
        num  = num-1
        for i in range(num):
            print(" "*((num-1)-i)+strings)
        
    else :
        num = num // 2
        for i in range(num):
            print(' ' * i + strings)
        
        for i in range(num):
            print(" "*((num -1)-i)+strings)




    pass


else :
    print("Size must be greater than 0.")