def combi(n,r):
    def fac(n):
        resultn = 1
        if n == 0:
            return 1
        for i in range (1 , n+1):
            resultn *= i 
        return resultn
    if r > n :
        return 0
    elif r == n :
        return 1 
    return fac(n)/(fac(n-r)*fac(r))

    # return fac(n,n)/(fac(n-r,n-r)*fac(r,r))

ans = (combi(4,3)+combi(7,3)+combi(3,3)+combi(7,3)+combi(10,3))/5
