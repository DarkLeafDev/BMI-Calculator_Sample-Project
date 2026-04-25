height = float(input("Enter Your Hight (In Meters) : "))
weight = int(input("Enter Your Weight (In Kilograms) : "))
bmi = weight / (height ** 2)
print("Your BMI is : ", bmi)
if bmi < 18.5:
    print("You are Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are Normal") 
elif bmi >= 25 and bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")