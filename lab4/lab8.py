depth = int(input("What is the well's depth? "))
jump = int(input("How high the frog can jump up? "))
slips = int(input("How far the frog slips down? "))

day = 0
leaps = 0
if jump - slips != 0:
    while depth - jump > 0 :
        day += 1
        leaps = depth - jump
        down = leaps + slips
        print(f"On day {day} the frog leaps to the depth of {leaps} meters.")
        print(f"At night he slips down to the depth of {down} meters.")
        depth = down
        if depth - jump <= 0 :
            print(f"The frog gets out of the well on day {day+1}.")
            break
elif depth == jump == slips :
    print("The frog gets out of the well on day 1.")
elif jump - slips == 0 :
    print("The frog will never escape from the well.")

