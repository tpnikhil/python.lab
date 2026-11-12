# University Scholarship Allocation

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    marks = int(input("Enter aggregate marks: "))
    s1 = int(input("Enter Subject 1 marks: "))
    s2 = int(input("Enter Subject 2 marks: "))
    attendance = int(input("Enter attendance percentage: "))
    income = int(input("Enter family income: "))

    # Check eligibility
    if (marks >= 75 and s1 >= 40 and s2 >= 40
        and attendance >= 75 and income <= 250000):

        students.append([name, marks, attendance])
        print("Eligible for Scholarship")

    else:
        print("Not Eligible for Scholarship")

# Rank students
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

# Display results
print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students")

else:
    rank = 1

    for student in students:
        print("Rank:", rank)
        print("Name:", student[0])
        print("Marks:", student[1])
        print("Attendance:", student[2])
        print("-------------------")
        rank += 1