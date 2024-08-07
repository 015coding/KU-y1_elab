score = []
count = 0

while True :
    sc = input("Input score (or ENTER to end): ")
    if sc == "" : 
        break
    count += 1
    score.append(int(sc))
    

avg = sum(score)/count
sum_sc = 0
for i in range (count) :
    sum_sc += (score[i]-avg)**2

sd = (sum_sc/(count-1))**0.5

print(f"Average score is {sum(score)/count:.2f}")
print(f"Standard deviation is {sd:.2f}")

for i in range (count):
    if score[i] >= avg+(1.5*sd) :
        print(f"Score #{i+1}: {score[i]} grade: A")
    elif score[i] >= avg+sd:
        print(f"Score #{i+1}: {score[i]} grade: B+")
    elif score[i] >= 0.5*sd + avg :
        print(f"Score #{i+1}: {score[i]} grade: B")
    elif score[i] >= avg:
        print(f"Score #{i+1}: {score[i]} grade: C+")
    elif score[i] >= avg - 0.5*sd :
        print(f"Score #{i+1}: {score[i]} grade: C")
    elif score[i] >= avg - sd :
        print(f"Score #{i+1}: {score[i]} grade: D+")
    elif score[i] >= avg - 1.5*sd :
        print(f"Score #{i+1}: {score[i]} grade: D")
    else :
        print(f"Score #{i+1}: {score[i]} grade: F")