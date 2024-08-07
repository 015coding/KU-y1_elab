initial = int(input("Enter initial amount in Baht: "))
interest = int(input("Enter interest rate in percent: "))

final1 = initial*(((100 + interest)/100))
final5 = initial*(((100 + interest)/100)**5)
final10 = initial*(((100 + interest)/100)**10)
final20 = initial*(((100 + interest)/100)**20)


print(f"Total amount after 1 year is {final1:.2f} Baht.")
print(f"Total amount after 5 years is {final5:.2f} Baht.")
print(f"Total amount after 10 years is {final10:.2f} Baht.")
print(f"Total amount after 20 years is {final20:.2f} Baht.")



