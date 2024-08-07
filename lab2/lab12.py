num = int(input("How long have Buzz played ?: "))

a = num // 60
b = num - a*60

if b > 20 :
    a += 1

if a <= 1:
    print(f"Total price is {a*900:.0f} baht.")
elif a < 4 :
    print(f"Total price is {a*900*0.9:.0f} baht.")
elif a < 5 or a == 4 :
    print(f"Total price is {a*900*0.8:.0f} baht.")
elif a >= 5 :
    print(f"Total price is {a*900*0.7:.0f} baht.")

