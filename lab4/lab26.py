
def remove(n):
    lst = []
    for i in range(len(n)):
        if n[i] != n[i-1]:
           lst.append(n[i])
    return lst



#a = eval("['a', 0, 0, 'b', 'b', 'b', 'c', 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]")
a = eval(input("InputList: "))
print(remove(a))