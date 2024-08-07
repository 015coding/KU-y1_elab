def list_factors(n):
    a = 1
    sumo = 0
    x = [i for i in range(1,n+1)
    if n%i == 0]
    return (" ".join(map(str , x)))

def find_sum_and_num_factors(n):
    count = 0
    check = 1
    sumo = 0
    while n / check != 1:
        if n % check == 0:
            sumo += check
            check += 1
            count += 1
        else:
            check += 1
    return sumo+n , count+1

inp = int(input("Enter positive number: ")) 
print(f"Factors of {inp} are")
print(list_factors(inp))
a , b = find_sum_and_num_factors(inp)
print(f"Sum of {list_factors(inp)} is {a}")
print(f"Number of factors is {b}")
if b == 2:
    print(f"{inp} is prime number.")
else :
    print(f"{inp} is not prime number.")