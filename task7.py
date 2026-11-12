# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

total_fare = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter travel distance in km: "))

    print("1. Sleeper")
    print("2. AC")
    print("3. General")

    choice = int(input("Select travel class: "))

    # Calculate basic fare based on distance
    if distance <= 100:
        fare = distance * 2
    elif distance <= 500:
        fare = distance * 3
    else:
        fare = distance * 4

    # Class charges
    if choice == 1:
        fare = fare + 100
        class_name = "Sleeper"
    elif choice == 2:
        fare = fare + 300
        class_name = "AC"
    elif choice == 3:
        fare = fare + 50
        class_name = "General"
    else:
        print("Invalid class selection!")
        continue

    # Age-based concession
    if age < 12:
        discount = fare * 0.50
    elif age >= 60:
        discount = fare * 0.30
    else:
        discount = 0

    fare = fare - discount

    # Reservation fee
    reservation = 50

    final_fare = fare + reservation

    # Cancellation option
    cancel = input("Do you want to cancel ticket? (yes/no): ")

    if cancel == "yes":
        penalty = final_fare * 0.25
        refund = final_fare - penalty
        print("Cancellation Penalty: Rs.", penalty)
        print("Refund Amount: Rs.", refund)
    else:
        penalty = 0
        refund = 0
        print("Ticket Confirmed!")

    # Display passenger details
    print("\n--- Passenger Bill ---")
    print("Name:", name)
    print("Age:", age)
    print("Class:", class_name)
    print("Distance:", distance, "KM")
    print("Discount: Rs.", round(discount, 2))
    print("Reservation Fee: Rs.", reservation)
    print("Final Fare: Rs.", round(final_fare, 2))

    if cancel == "yes":
        print("Refund: Rs.", round(refund, 2))

    total_fare = total_fare + final_fare

print("\nTotal Booking Amount: Rs.", round(total_fare, 2))