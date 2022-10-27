height=input("enter your height in m: ")
weight=input("enter your weight in kg: ")

height=float(height)
weight=int(weight)

BMI=weight/height**2
# BMI as a whole number
BMI=int(BMI)

print("BMI is: ",BMI)