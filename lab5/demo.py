strings1 = ["Twostringsaresaidtobe", "completeifonconcatenation"]
strings2 = ["abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyz"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
al = []
check = []
count = 0
result = []

for itema in alphabet:
    al.append(itema)
for item1 in strings1:
    for item2 in strings2:
        x = item1 + item2
        ga = []

        for item_x in x:
            ga.append(item_x)
        for item in al:
            if item not in x:
                result.append(item)
        if len(result) == 0:
            result.append(x)
            count +=1

print(f"Output: {count}")
print("The total complete pairs that are forming are:")
print(result)