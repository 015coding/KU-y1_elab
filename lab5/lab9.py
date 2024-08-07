def commaCode(myList):
    if not myList:
        print("")
    if isinstance(myList, list):
        a = myList
    else:
        a = myList.split()
    lst = []
    x = 0
    if myList:
        if len(a) == 0:
            print("[]")
        if len(a) == 1:
            print(f"{a[0]}")
        else:
            while x + 1 < len(a):
                print(f"{a[x]},", end=" ")
                x += 1
            else:
                print(f"and {a[x]}")
    elif not myList:
        print("")


myList = input("Input: ")
commaCode(myList)


