score = []
count = 0

while True :
    sc = input("Input score (or ENTER to end): ")
    if sc == "" :
        break
    count += 1
    score.append(int(sc))

score.sort()

for i in range (count):
    print(f"Rank #{i+1}: {score[count-1-i]}")
