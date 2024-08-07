def create_matrix(rows, cols, location):
    detect_rows = [-1, 0, 1]
    detect_cols = [-1, 0, 1]

    matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for item in location:
        a, b = map(int, item)
        if 0 <= a < rows and 0 <= b < cols:
            matrix[b][a] = "X"

    for i in range(rows):
        for j in range(cols):
            if matrix[j][i] != 'X':
                count = 0
                for x in detect_rows:
                    for y in detect_cols:
                        ni, nj = i + x , j + y
                        if 0 <= ni < rows and 0 <= nj < cols and matrix[nj][ni] == "X":

                            count += 1
                matrix[j][i] = count
    return matrix

def print_ga(matrix):
    for rows in matrix:
        print(' '.join(str(a) for a in rows))


grid = input("Grid Size: ").split()
rows, cols = map(int, grid)

num = int(input("Number of mine(s): "))
locate = []
for i in range(num):
    bomb = input(f"Mine#{i+1}: ").split()
    locate.append(bomb)

create_matrix(rows, cols, locate)
print_ga(create_matrix(rows, cols, locate))
