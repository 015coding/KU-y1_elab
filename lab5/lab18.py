#strings1 = ["abcdefgh", "geeksforgeeks", "lmnopqrst", "abc"]
#strings2 = ["ijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"]
strings1 = eval(input("String set1: "))
strings2 = eval(input("String set2: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"
al = []
check = []
gay = []
count = 0
def check(lists,alpha):
    ga = []
    result = []
    for item_x in lists:
        ga.append(item_x)
    for item in alpha:
        if item not in lists:
            result.append(item)
    if len(result) == 0:
        return lists


for itema in alphabet:
    al.append(itema)
for item1 in strings1:
    for item2 in strings2:
        x = item1+item2
        gay.append(check(x, al))

for item in gay:
    if item != None:
        count +=1
print(f"Output: {count}")
print("The total complete pairs that are forming are:")
for item in gay:
    if item != None:
        print(f" {item}")


