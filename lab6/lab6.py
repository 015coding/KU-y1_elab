a, b = str(input("City Size: ")).split()
a = int(a)
b = int(b)
#city = [[2 ,3 ,5 ,6 ,2],[1,3,4,7,1], [6, 5, 4, 1, 3], [2, 3, 7, 9, 6]]
city = []
for i in range(a):
    mung = input("").split()
    city.append(mung)
N_view = city
W_view = city
S_view = city
E_view = city
def N(a,b,city):
    max = 0
    count = b
    for i in range(b):
        for j in range(a):
            if max == 0:
                max = city[j][i]
            elif city[j][i] > max:
                max = city[j][i]
                count += 1
        max = 0
    return count
def S(a,b,city):
    max = 0
    count = b
    for i in range(0,b-1,1):
        for j in range(a-1,0,-1):
            if max == 0:
                max = city[j][i]
            elif city[j][i] > max:
                max = city[j][i]
                count += 1
        max = 0
    return count

def E(a,b,city):
    max = 0
    count = a
    for i in range(0,a,1):
        for j in range(b-1,-1,-1):
            if max == 0:
                max = city[i][j]
            elif city[i][j] > max:
                max = city[i][j]
                count += 1
        max = 0
    return count

def W(a,b,city):
    max = 0
    count = a
    for i in range(0,a):
        for j in range(0,b,1):
            if max == 0:
                max = city[i][j]
            elif city[i][j] > max:
                max = city[i][j]
                count += 1
        max = 0
    return count
N = N(a,b,N_view)
S = S(a, b, S_view)
E = E(a, b, E_view)
W = W(a, b, W_view)

if N == S == E == W:
    print("N S E W")
else:
    dic = {}
    dic['N'] = N
    dic['S'] = S
    dic['W'] = W
    dic['E'] = E
    max_a = max(dic.values())
    for i,k in dic.items():
        if k == max_a:
            print(i)


