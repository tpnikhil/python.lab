student1 = int(input("Enter the name of Student 1: "))
student2 = int(input("Enter the name of Student 2: "))

marks1 = float(input("Enter marks of Student 1: "))
marks2 = float(input("Enter marks of Student 2: "))

average = (marks1 + marks2) / 2

print("Average marks:", average)

if marks1 > marks2:
    print(student1, "scored higher.")
elif marks2 > marks1:
    print(student2, "scored higher.")
else:
    print("Both students scored equal marks.")