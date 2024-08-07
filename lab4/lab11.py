day = int(input("Day: "))


num1 = 0
num2 = 1
nextnumber = num2
print(1 , end = " ")
for i in range (day-1) :
    print(nextnumber , end = " ")
    num1 , num2 = num2 , nextnumber
    nextnumber = num1 + num2
