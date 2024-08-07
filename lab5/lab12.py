n, m = map(int, input("").split())

time_lst = []

for i in range(n):
    t = int(input())
    time_lst.append(t)

r = max(time_lst)*m
l = 1

while l <= r:
    midium = (r+l)//2
    count = 0
    for i in time_lst:
        count += (midium//i)

    if count >= m:
        r = midium - 1

    else:
        l = midium + 1

print(l)