
def group(n):
    lst = []
    i = 0
    while i < len(n):
        x = [n[i]]
        while i+1 <len(n) and n[i + 1] == n[i]:
            x.append(n[i + 1])
            i += 1
        lst.append(x)
        i += 1
    return lst



#a = eval("[0, 0, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 7, 7, 7, 7, 1, 1]")
a = eval(input("InputList: "))
print(group(a))
