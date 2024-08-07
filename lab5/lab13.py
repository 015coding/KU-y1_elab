import math
num = input("").split()
x = 0
for i in num:
    x += int(i)
print(math.ceil(x/4))
