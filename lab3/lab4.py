def fibonacci(n):
    if n == 1 :
        return n == 1
    elif n == 2 :
        return n ==2
    else :
        return fibonacci(n -1) + fibonacci(n -2)

n = int(input("Enter n: "))
print(f'fibo({n}) = %d' % fibonacci(n))