a = []
while True:
    num = input("")
    a.append(int(num))
    if num == "0":
        break


def find_number(lst):
    if not lst:
        return None, 0

    max_count = 1
    count = 1
    most_frequent = lst[0]


    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1

        else:
            count = 1

        if count > max_count:
            max_count = count
            most_frequent = lst[i]

    return most_frequent, max_count


number, max_A = find_number(a)
print(max_A)
print(number)