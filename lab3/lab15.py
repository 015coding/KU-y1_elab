def change(baht, baht_1):
    if baht >= baht_1:
        return baht // baht_1
    else:
        return 0

money = int(input("Enter total money: "))

b500 = change(money, 500)
left = money - (b500 * 500)

b100 = change(left, 100)
left = left - (b100 * 100)

b20 = change(left, 20)
left = left - (b20 * 20)

b5 = change(left, 5)
left = left - (b5 * 5)

b1 = left

print("500:", b500)
print("100:", b100)
print(" 20:", b20)
print("  5:", b5)
print("  1:", b1)