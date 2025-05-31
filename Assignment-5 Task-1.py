# Task 1: Create a Dictionary of Student Marks

students = {'Alice':85, 'Martha': 75, 'Nancy': 65}
name = input("Enter the Student's name:")

if name in students:
    print(name + "'s marks:", students[name])
else:
    print("Student not found.")