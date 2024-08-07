A = list(map(int,input().split()))
menu,x = input().split()

while menu != "E" and x != 0:
    if menu == "A":
        final =A.append(x)
        menu,x = input().split()
    if menu == "S":
        final_len = len(A)
        if final_len >= int(x) :
            print(A[int(x)])
        menu,x = input().split()
    if menu == "R":
        del A[int(x)]
        menu,x = input().split()
else :
    for i in range (len(A)):
        print(A[i] , end=" ")

