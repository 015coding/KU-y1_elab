def warship(row ,col):

    a = row
    b = col
    for i in range(8):
        print("-----------------")
        for j in range(8):
            if i == a and j == b:
                print("|R", end="")
            elif i == a or j == b:
                print("|x", end="")
            else:
                print("|", end=" ")

        print("|")
    print("-----------------")



rows = int(input("Enter Rook's row position: "))
cols = int(input("Enter Rook's column position: "))

warship(rows, cols)
