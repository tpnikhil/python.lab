# Progressive Electricity Billing

bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    units = int(input("Enter electricity units: "))

    # Calculate bill using slabs
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charges
    bill = bill + 50

    # Surcharge
    surcharge = bill * 0.05
    bill = bill + surcharge

    # Rebate for low consumption
    if units <= 100:
        bill = bill - 20

    bills.append(bill)

    print("Total Electricity Bill: Rs.", round(bill, 2))

# Compare monthly bills
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 500:
            print("Warning: Unusual increase in bill!")

        elif increase > 0:
            print("Bill increased by Rs.", round(increase, 2))

        else:
            print("Bill decreased or remained same.")