import random

name_string=input("Enter the names of friends: ")
names=name_string.split(", ")

random_choice=random.randint(0,len(names)-1)
person_who_will_pay=names[random_choice]

print(f"Thank you for paying the bill {person_who_will_pay}")
