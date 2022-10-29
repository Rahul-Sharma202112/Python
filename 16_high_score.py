student_marks=input("Input the list of student marks :").split()
for n in range(0,len(student_marks)):
    student_marks[n]=int(student_marks[n])
print(student_marks)

highest_marks=0
for marks in student_marks:
    if marks > highest_marks:
        highest_marks=marks
print(f"Highest marks in the class is: {highest_marks}")
