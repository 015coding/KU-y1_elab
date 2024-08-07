tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))

total = (6000*tv) + (1500*dvd) + (3000*audio)
print(f"Total price is {total:.2f} baht.")

if total >= 24000:
    final = (total *0.2)
    print(f"You've got a discount of {final:.2f} baht.")
    final1 = (total * 0.8)
    print(f"Your payment is {final1:.2f} baht. Thank you!")
else :
    print(f"Your payment is {total:.2f} baht. Thank you!")