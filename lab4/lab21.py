def countStr(strings):
    count = 0
    for a in strings:
        if len(a) >= 2:
            if a[0] == a[-1]:
                count +=1

    return count


strings = str(input("Enter a set of strings: ")).split()
print(countStr(strings))