def countConsec(lst):
    lens = len(lst)
    lst_a = []
    count = 0
    for i in range(1, lens):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            lst_a.append((lst[i-1], count+1))
            count = 0
    lst_a.append((lst[lens-1], count + 1))
    return lst_a


lst_inp = eval(input(str("Enter a list of objects: ")))
if lst_inp:
    a = countConsec(lst_inp)
    e, c = max(a, key=lambda x:x[1])
    print(e)
    print(c)
else:
    print("Nothing to do.")


