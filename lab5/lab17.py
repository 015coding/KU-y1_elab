string1 = input("Input string: ")
string2 = input("Input string: ")
st1 = []
st2 = []
for item in string1:
    st1.append(item)
for item in string2:
    st2.append(item)

def intercept(st1,st2):
    result = []
    for item in st1:
        if item not in st2:
            result.append(item)
    for item in st2:
        if item not in st1:
            result.append(item)
    x= ''.join(result)
    return x

print(intercept(st1, st2))