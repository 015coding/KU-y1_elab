x =0
numbers = []
while True:
    num = input("Enter a number (just [Enter] to stop): ")
    if num == "":
        break
    x+=1
    numbers.append(float(num))

if len(numbers) != 0:
    numbers.sort()
    max = numbers[x-1]
    min = numbers[0]
    a = sum(numbers) / x
    print(f"The maximum value is {max:.2f}")
    print(f"The minimum value is {min:.2f}")
    print(f"The average value is {a:.2f}")    
else:
    print("Nothing to do.")
