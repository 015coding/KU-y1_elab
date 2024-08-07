def check(x, y, num):
    if x < 0 or x >= num or y < 0 or y >= num:
        return False
    return True


row = [-2, -1, 0, 1, 2]
col = [-2, -1, 0, 1, 2]

num = int(input())
state = []
area = []
for i in range(num):
    text = input()

    for m in range(len(text)):
        x = i
        y = m
        if text[m] == "G":
            for j in range(len(row)):
                for k in range(len(col)):
                    newX = x + row[j]
                    newY = y + col[k]
                    if check(newX, newY, num):
                        area.append([newX, newY])
        if text[m] == "E":
            state.append([x, y])

counter = 0
for position in state:
    if position in area:
        counter += 1

print(counter)
