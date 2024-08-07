def factorial(x):
    a = 0
    final = 1
    sumo = 0
    for i in range (x):
        
        a += 1
        final *= a
        sumo += final
        
    return sumo 


x = int(input("Input k: "))
count = 0   
final2 = 1
for i in range (x):
    count += 1
    final2 *= count
    print(f"{count}! = {final2}")

print(f'Summation of factorial 1!-{x}! = {factorial(x)}')