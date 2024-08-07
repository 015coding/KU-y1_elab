level = int(input("How many levels? "))
size = int(input("Enter bush size: "))

c = 0
a = size -1
b =1
while c <level:
    for j in range (size):
        print(" "*a+"*"*b)
        a -= 1
        b +=2
    a = size -1
    b =1
    c += 1