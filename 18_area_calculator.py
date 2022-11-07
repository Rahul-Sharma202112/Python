import math

def area_of_wall(Height,Width):
    coverage_per_can=5
    Num_of_cans=math.ceil((Height*Width)/coverage_per_can)
    print(f"You need {Num_of_cans} cans of Paint.")

height=int(input("Height of wall :"))
width=int(input("weidth of wall :"))

area_of_wall(height,width)
