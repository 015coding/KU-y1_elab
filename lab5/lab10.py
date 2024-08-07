list_inp = [int(i) for i in input("").split()]
x = 0
y = 0
length = len(list_inp)

while x <= y:
    xy = input("").split()
    x = int(xy[0])
    y = int(xy[1])

    if x < 0:
        x += length
    if y < 0:
        y += length

    asw = 0
    if x < 0 or x > length-1:
        if y < 0 or y > length-1:
            print("x and y Bad Input")
            x = 0
            y = 0
        elif y >= 0 or y <= length-1:
            print("x Bad Input")
            x = 0
            y = 0
        else:
            print("y Bad Input")
            x = 0
            y = 0

    elif x == 0 or x == length-1:
        if y < 0 or y > length-1:
            print("y Bad Input")
            x = 0
            y = 0
        elif x > y:
            break
        else:
            print(sum(list_inp[x:y+1]))
    elif x > y:
        break
    else:
        print(sum(list_inp[x:y + 1]))




