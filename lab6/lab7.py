def flip(option,lst):
    len_ls = len(lst)
    if option == "V":
        print("After flip: ")
        for i in range(len_ls-1, -1, -1):
            print(' '.join(str(a) for a in lst[i]))
    elif option == "H":
        print("After flip: ")
        for row in lst:

            print(' '.join(str(a) for a in reversed(row)))

option = input("Direction to flip square (V/H): ")
num = int(input("Input size of square: "))
lst = []
if num != 0:
    for i in range(num):
        a = input("").split()
        lst.append(a)

    flip(option, lst)