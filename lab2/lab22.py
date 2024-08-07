day = int(input("How many day : "))
summary = 0

for i in range (day):
    price = float(input(f"Input price in day {i+1} : "))
    if i == 0 :
        summary += (price*0.95)
    else:
        summary += (price*(0.95-(i*0.01)))

print(f"Summary price = {summary:.2f}")