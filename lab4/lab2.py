number = []
x = 0
while True:    
    num = input("Enter a number (to exit, just enter zero): ")
    if num == "0":
        break
    x += 1
    number.append(float(num))
num_len = len(number)
num_p = 0
num_n = 0
for i in range (x):
    if number[i] >=0 :
        num_p += number[i]
    else:
        num_n += number[i]

print(f"Sum of all positive numbers is {num_p:.2f}")
print(f"Sum of all negative numbers is {num_n:.2f}")


