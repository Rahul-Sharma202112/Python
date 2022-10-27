#Nested if else condition
print("Welcome to rollercoaster")
height=int(input("Enter your height:"))

if height>120:
    print("You can ride rollercoaster!")
    age=int(input("Enter your age:"))
    if age>18:
        print("You have to pay $12.")
    elif age>=12:
        print("You have to pay $7.")
    else:
        print("You have to pay $5.")
else:
    print("Sorry you can't ride.")        
