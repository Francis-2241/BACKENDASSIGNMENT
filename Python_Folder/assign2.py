# Second ASSIGNMENT 
# Create a list of students names, and print each using for loop. 

students_name = ["Joe","Anderson","Emmanuel","David",]
for students_name in ["Joe","Anderson","Emmanuel","David",]:
    print(students_name)


# Write a python program using while loop to create a simple banking system:
# balance of 0, to allow user check balance and deposit money, withdraw money and exits.

balance = 0  # Starting balance
running = True  # Control variable for the while loop

while running:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"₦{amount} deposited successfully!")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: $"))
        if amount > balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            balance -= amount
            print(f"₦{amount} withdrawn successfully!")

    elif choice == "4":
        print("Thank you for using our banking system. Goodbye!")
        running = False

