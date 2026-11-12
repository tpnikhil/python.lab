# Hospital Billing and Patient Classification

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))

    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    # Validate billing details
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges!")
        continue

    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply concession
    if age >= 60:
        discount = total * 0.20
    elif total >= 10000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    # Patient classification
    if final_bill <= 5000:
        category = "Low Payment"
    elif final_bill <= 15000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    # Display bill
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Charges: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final_bill)
    print("Patient Category:", category)

    if final_bill == 0:
        print("Payment Status: No Payment Due")
    else:
        print("Payment Status: Payment Required")