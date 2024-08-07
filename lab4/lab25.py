a = eval(input("Original list: "))
lst = []

def flatten(n):
    for item in n:
        if isinstance(item, list):
            flatten(item)
        else:
            lst.append(item)
    return lst


print(f"Flatten list: {flatten(a)}")