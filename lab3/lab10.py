import math
#area = 0
def MiniHeart(l):
    area = (l**2) + (math.pi + (l/2)**2)
    #print(area)
    return int(area)

ent = int(input("Please enter the value of L: "))


print("Area is " , format(MiniHeart(ent),"%.4f"))

