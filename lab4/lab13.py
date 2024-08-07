police_d = 0
criminal_d = 100
n = 0
while police_d < criminal_d :
    distance = int(input("Input distance: "))
    n += 1
    criminal_d += 2**n 
    police_d += distance
    print(f"Police distance: {police_d:.0f}")
    print(f"Criminal distance: {criminal_d:.0f}")
else :
    print("Caught him!")