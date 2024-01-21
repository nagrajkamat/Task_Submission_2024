import datetime

# Expense tracker data structure
expenses = {}

def add_expense(date, category, amount):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({"category": category, "amount": amount})
    print(f"Expense of ${amount:.2f} in category '{category}' added on {date}.")

def view_expenses():
    for date, items in expenses.items():
        print(f"\nExpenses on {date}:")
        for item in items:
            print(f"Category: {item['category']}, Amount: ${item['amount']:.2f}")

def analyze_spending():
    total_spending = sum(item['amount'] for items in expenses.values() for item in items)
    print(f"\nTotal spending: ${total_spending:.2f}")

# Main loop for the expense tracker
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        date_str = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        amount = float(input("Enter the expense amount: "))
        
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date().strftime("%Y-%m-%d")
            add_expense(date, category, amount)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        analyze_spending()

    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
