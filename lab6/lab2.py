text = input("Input sentence: ")
n = int(input("Input row: "))
x = 0
shift = 1
new_arr = ['']*n
for i in range(len(text)):
    new_arr[x] += text[i]
    if x < n-1 and shift == 1:
        x += 1
    elif x > 0 and shift == -1:
        x -= 1
    else:
        shift *= -1
        x += shift
print("".join(new_arr))