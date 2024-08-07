num = int(input("Input number: "))
odd = num % 2
while odd == 0 :
    print("Please input odd number")
    num = int(input("Input number: "))
    odd = num % 2
    
for i in range (num) :
    print("x" * (i+1) )
for i in range (num):
    print("x" * ((num-1) - i ))