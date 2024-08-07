m = int(input("M: "))
n = int(input("N: "))
mcal1 = m *2
mcal2 = m *6
ncal1 = n
ncal2 = n*4
cal1 = mcal1 + ncal1
cal2 = mcal2 + ncal2


if m < 1000000 and m >= 0 and n < 1000000 and m >= 0 :
    print(f"{cal1} {cal2}")
else :
    pass
