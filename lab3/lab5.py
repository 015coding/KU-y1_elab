def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        memo[n] = result
        return result

    
n = int(input("Enter n: "))
print(f'fibo({n}) = %d' % fibonacci(n))