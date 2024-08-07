def box(n):
    count = 0
    space = 0
    space_mid = n
    x = 0
    for i in range(n):
        if count == 0 or count == n - 1:
            print("." * (n))
            count += 1
        if count > 0 and count <= n // 2 - 1:
            print("." + " " * space + "." + " " * (space_mid - 4) + "." + " " * space + ".")
            space_mid -= 2
            space += 1

        elif count == n // 2:
            print("." + " " * (n // 2 - 1) + "." + " " * ((n // 2) - 1) + ".")
        else:
            space -= 1
            space_mid += 2
            print("." + " " * space + "." + " " * (space_mid - 4) + "." + " " * space + ".")
            if space_mid > n - 2:
                print("." * (n))
                break

        count += 1


n = int(input())
if n >= 9 and n % 2 != 0:
    box(n)