d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))
#d = 31
#m = 12
#y = 1996

if y % 4 == 0:
    if y % 100==0:
        y_2 = 28
    elif y % 400==0:
        y_2 = 29
    else :
        y_2 = 29
    
else :
    y_2 = 28

def mo(m):
    if m==1:
        return int(31)
    elif m==2:
        return 0
    elif m==3:return int(31)
    elif m==4:return int(30)
    elif m==5:return int(31)
    elif m==6:return int(30)
    elif m==7:return int(31)
    elif m==8:return int(31)
    elif m==9:return int(30)
    elif m==10:return int(31)
    elif m==11:return int(30)
    elif m==12:return int(31)
su = 0
x =1
for i in range(m-1):
    su += mo(int(x))
    x +=1
if m <2 :
    print(su+d)
elif m == 2:
    print(d+su)
else :
    print(su+d+y_2)
    