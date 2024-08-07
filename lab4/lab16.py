def alternative_sum(n):
    sumo = 0
    for i in range (1 , n+1) :
        if i % 2 != 0 :
            sumo += i
        else :
            sumo -= i
    return sumo

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n ,alternative_sum(n)))