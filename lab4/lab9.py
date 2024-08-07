y = 0

z = 0
def plus(total,value) :
    y = total *value
    return y 

def minus(total,value) :
    z = total  * value
    return z

count = input("How many food you have : ")
count = int(count)
s =0
for i in range (count) :
    x = input().split()
    if x[1] == "1" :
        s = plus(int(x[0]),int(x[1])) +s
        
    elif x[1] == "-1" :
        s = minus(int(x[0]),int(x[1]))+s



print(s)

        
