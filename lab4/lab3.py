score = []
count = 0
while True:
    sc = input("Input score (or ENTER to end): ")
    if sc == "":
        break
    count += 1
    score.append(float(sc))



for i in range (count):
    print(f"Score #{i+1}: {score[i]}")
print(f"Average score is {(sum(score)/count):.2f}")
print(f"Minimum score is {min(score):.0f}")
print(f"Maximum score is {max(score):.0f}")