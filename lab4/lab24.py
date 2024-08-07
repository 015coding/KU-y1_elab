

def pair(n):
    lst = []
    n = list(map(int ,n))
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if abs(n[i] - n[j]) == 3:
                lst.append([n[i], n[j]])
    return lst




number = input("Enter list of number: ")

lst_num = number.split()


print(f"Output list: {pair(lst_num)}")
