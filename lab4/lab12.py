time = int(input("Estimated time : "))
sum_w = time * 2.5
week = 1
week_lose = time // 8
phy = 0
wei = 0
fit = 0
while week <= week_lose:
    print(f"Week{week}")
    phy1 = int(input("Physical therapy : "))
    wei1 = int(input("Weight training : "))
    fit1 = int(input("Fitness training : "))
    phy += phy1
    wei += wei1
    fit += fit1
    week += 1
    if phy >= sum_w and wei >= sum_w and fit >= sum_w:
        print("Buzzy has recovered in time.")
        break


else:
    print("Buzzy has not recovered in time.")
