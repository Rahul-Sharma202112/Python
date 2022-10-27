#Multiple condition
print("Welcome to rollercoaster")
height=int(input("Enter your height:"))

bill=0
if height>120:
    print("You can ride rollercoaster!")
    age=int(input("Enter your age:"))
    if age>18:
        bill=12
        print("You have to pay $12.")
    elif age>=12:
        bill=7
        print("You have to pay $7.")
    else:
        bill=5
        print("You have to pay $5.")

    want_photos=input("You want some photos ,Y or N .")
    if want_photos=="Y":
        bill=bill+15
    
    print(f"Your final bill is {bill}")

else:
    print("Sorry you can't ride.")        
