weight = int(input("Weight: "))
height = int(input("Height: "))

bmi = weight/((height/100)**2)

if bmi <= 18.6 :
    print(f"Your BMI is {bmi:.1f} You're in the underweight range.")
elif bmi <= 25 :
    print(f"Your BMI is {bmi:.1f} You're in the healthy weight range.")
elif bmi <= 30 :
    print(f"Your BMI is {bmi:.1f} You're in the overweight range.")
else :
    print(f"Your BMI is {bmi:.1f} You're in the obese range.")


