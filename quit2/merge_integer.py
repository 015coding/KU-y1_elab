def merge(a, b):
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)
    merge_lst = []

    def ascii_encode(x):
        return [ord(item) for item in x]
    if isinstance(a[0], str) and a[0].isalpha():
        ord_a = [ascii_encode(str(item)) for item in a]
        ord_b = [ascii_encode(str(item)) for item in b]

        while i < len_a and j < len_b:
            if ord_a[i] < ord_b[j]:
                merge_lst.append(a[i])
                i += 1
            else:
                merge_lst.append(b[j])
                j += 1
    else:
        while i < len_a and j < len_b:
            if a[i] < b[j]:
                merge_lst.append(a[i])
                i += 1
            else:
                merge_lst.append(b[j])
                j += 1

    while i < len(a) :
        merge_lst.append(a[i])
        i += 1
    while j < len(b):
        merge_lst.append(b[j])
        j += 1

    return merge_lst



#num1 = eval("[-30]")
#num2 = eval("[-87, -82, -71, -61, -57, -10, 48, 48, 66, 68]")

num1 = eval(input("Enter list a: "))
num2 = eval(input("Enter list b: "))

print(merge(num1, num2))

