def isPrime(number):
    if number <= 1 :
        return False
    if number == 2 :
        return True
    if number % 2 == 0 :
        return False
    for i in range (3,int(number**0.5) +1 , 2):
        if number % i == 0 :
            return False
    return True

def printAllPrimes(limit):
    primes = [i for i in range(2,limit+1)
    if isPrime(i)]
    print(" ".join(map(str , primes)))
    
number = int(input("Input n: "))
printAllPrimes(number)
        