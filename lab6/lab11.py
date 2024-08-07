def shift(y, txt):
    a = len(txt)
    txt_sp = txt

    count = 0
    pr_x = 0
    con = 0
    result = []
    for item in txt_sp[0]:
        con +=1
    while count < a:
        while count < y:
            result.append("0"*con)
            count += 1

        if count == a:
            break
        else:
            result.append(txt_sp[pr_x])
            pr_x += 1
            count += 1
    return result
def shiftX(x,result):
    len_a = len(result[0])
    len_row = len(result)
    count_str = 0
    final = []
    for i in range(len_row):
        print("0"*x, end="")
        for j in range(len_a-x):
            print(result[i][j],end= "")
        print()

X_shift = int(input("Enter horizontal shift size: "))
Y_shift = int(input("Enter vertical shift size: "))
strings = []
int_str = 0
print("Enter image:")
while True:
    if int_str != "-1":
        int_str = input("")
        strings.append(int_str)
    else :
        break
strings.remove("-1")


#a = "tttttttttttttt tt----tt----tt tt----tt----tt tt----tt----tt tttttttttttttt tttttttttttttt tttttt--tttttt tttttttttttttt tttttttttttttt"
x = shift(Y_shift, strings)
print("After shift:")
shiftX(X_shift,x)



