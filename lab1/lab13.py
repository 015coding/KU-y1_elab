small = int(input("A : "))
Big = int(input("B : "))
range = int(input("X : "))

time = range/Big
time_arrive = ((range - (small*time)) / small) *3600
time_arrive = int(time_arrive)

print(f"Wait : {time_arrive} sec")


