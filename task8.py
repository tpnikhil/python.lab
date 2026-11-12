# ATM Transaction Sequence Simulation

balance = 5000
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):

    print("\n1. Deposit")
    print("2. Withdraw")

    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount!")

    elif choice == 1:
        balance = balance + amount
        transactions.append("Deposit: Rs." + str(amount))
        print("Amount Deposited Successfully")

    elif choice == 2:

        if amount > 10000:
            print("Withdrawal limit exceeded!")

        elif amount > balance:
            print("Insufficient Balance!")

        else:
            balance = balance - amount
            transactions.append("Withdrawal: Rs." + str(amount))
            print("Amount Withdrawn Successfully")

    else:
        print("Invalid Transaction!")

# Display transaction summary

print("\n--- ATM Transaction Summary ---")

for transaction in transactions:
    print(transaction)

print("\nTotal Transactions:", len(transactions))
print("Final Balance: Rs.", balance)