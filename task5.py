# Employee Payroll and Deduction Analysis

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter employee name: ")

    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowances: "))
    overtime = float(input("Enter overtime amount: "))
    incentive = float(input("Enter incentives: "))

    # Calculate gross salary
    gross = basic + allowance + overtime + incentive

    # Calculate progressive deductions
    if gross <= 10000:
        deduction = gross * 0.05
    elif gross <= 20000:
        deduction = (10000 * 0.05) + (gross - 10000) * 0.10
    else:
        deduction = (10000 * 0.05) + (10000 * 0.10) + (gross - 20000) * 0.15

    # Calculate net salary
    net_salary = gross - deduction

    # Display salary statement
    print("\n------ Salary Statement ------")
    print("Employee Name:", name)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowance)
    print("Overtime: Rs.", overtime)
    print("Incentives: Rs.", incentive)
    print("------------------------------")
    print("Gross Salary: Rs.", gross)
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net_salary, 2))
    print("------------------------------")