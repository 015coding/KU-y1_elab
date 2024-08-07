def nb_year(p0, peresnt,aug, p):
    a = 0
    while p0 < p :
        p0 = int(p0+(p0*(peresnt/100))+aug)
        a += 1
    return a


print(nb_year(1500000, 0.25, -1000, 2000000))