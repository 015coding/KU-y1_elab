def simple_interest(p , r , t):
    return (p*r*t/100) + p
    

def compound_interest(p,r,t):
    return p * ((1+(r/100))**t)

p= int(input("Enter principle: "))
r =  float(input("Enter interest rate: "))
t= float(input("Enter time: "))

print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))