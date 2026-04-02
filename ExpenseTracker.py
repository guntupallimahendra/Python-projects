# Expense Tracker Application by Mahendra

expenses = []   


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food, Travel, Study, etc.): ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: {expense['amount']}, "
              f"Category: {expense['category']}, "
              f"Description: {expense['description']}")
    print()


def total_expense():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total}\n")


def category_wise_expense():
    category_total = {}

    for expense in expenses:
        category = expense["category"]
        category_total[category] = category_total.get(category, 0) + expense["amount"]

    print("\n--- Category-wise Expense ---")
    for category, amount in category_total.items():
        print(f"{category}: ₹{amount}")
    print()


def main_menu():
    while True:
        print("=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            category_wise_expense()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")



main_menu()
