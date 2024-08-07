
def sqrt(number):
    num = 0 
    sumo = 0
    while sumo < number :    
        num += 1
        sumo = num*num
        if sumo > number :
            print("can,t squ")
        elif sumo == number :
            print(num)
number = int(input("number : ")) 
sqrt(number)
