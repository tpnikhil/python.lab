# Mobile Plan Cost Optimization

plans = [
    ["Plan A", 199, 2, 100, 28],
    ["Plan B", 299, 3, 200, 56],
    ["Plan C", 399, 5, 300, 84],
    ["Plan D", 499, 7, 500, 84]
]

data = float(input("Enter your monthly data usage (GB): "))
validity = int(input("Enter required validity (days): "))
budget = int(input("Enter your budget (Rs.): "))

best_plan = ""
lowest_cost = 99999

print("\n--- Available Mobile Plans ---")

for plan in plans:

    name = plan[0]
    price = plan[1]
    data_limit = plan[2]
    excess_rate = plan[3]
    days = plan[4]

    # Calculate excess charges
    if data > data_limit:
        extra = data - data_limit
        excess = extra * excess_rate
    else:
        excess = 0

    total_cost = price + excess

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Excess Charge: Rs.", excess)
    print("Total Cost: Rs.", total_cost)

    # Check plan eligibility
    if data <= data_limit and days >= validity and total_cost <= budget:

        if total_cost < lowest_cost:
            lowest_cost = total_cost
            best_plan = name

# Display best plan
print("\n--- Best Mobile Plan ---")

if best_plan == "":
    print("No suitable plan found")

else:
    print("Most Economical Plan:", best_plan)
    print("Total Cost: Rs.", lowest_cost)