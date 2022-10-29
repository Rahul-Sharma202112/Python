# Average height using for loop instead of using sum function.
student_height=input("Input a list of student heights ").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)

total_height=0
for height in student_height:
    total_height+=height
# print(total_height)

num_of_students=0
for student in student_height:
    num_of_students+=1
# print(num_of_students)

average_height=total_height//num_of_students
print(average_height)