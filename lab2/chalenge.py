num = 17

check = num %2
if check != 0 :
    n = 0
    n2 = (num-1)//2
    re = 3
    x = num
    y= num
    for i in range ((num+1)//2) :
        
        print(' '*n ,'*'*x)
        x -=2
        n += 1 
        
    
    for i in range((num-1)//2):
        
        n2 -= 1
        print(' '*n2 , "*"*re)
        re +=2
        
