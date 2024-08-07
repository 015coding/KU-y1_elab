#n = int(input("Enter the number of rows or columns : "))
n = 10
count = 1
start_num = 1

while count <= n:
    for i in range(count, n+count):
        if start_num == count:

            print(f'%2d' % start_num, end=" ")

        #print(start_num, end=" ")

        else:
            print(f'%2d' % start_num, end=" ")
        start_num += 1
    print()
    count += 1
    start_num = count