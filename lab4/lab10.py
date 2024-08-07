point = int(input("Distance from starting point(m.): "))
if point != 0 :
    x = 0
    a = 0
    b = 0
    count = 0
    while b < point :
        x =  a + 5
        print(x , end = " ")
        b = x-2
        print(b , end = " ")
        a = b
        count += 1

    x = 0
    a = b
    while b > point :
        x =  a - 4
        print(x , end = " ")
        b = x+3
        print(b , end = " ")
        a = b
        count += 1
    print()
    print(f"Buzz moved {count} set(s)")
else :
    print(0)