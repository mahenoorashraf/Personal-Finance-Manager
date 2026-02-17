print("THIS IS THE NEW MENU FILE")
from expense import Expense
from utils import validate_amount
from reports import show_all_expenses, category_summary, monthly_report
from file_manager import backup_data


def show_menu():
    print("\n==== PERSONAL FINANCE MANAGER ====")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Category-wise Summary")
    print("4. Generate Monthly Report")
    print("5. Search Expenses")
    print("6. Backup Data")
    print("7. Exit")


def search_expense(expenses):
    keyword = input("Enter keyword to search: ").lower()

    found = False
    for expense in expenses:
        if keyword in expense.description.lower() or keyword in expense.category.lower():
            print(expense)
            found = True

    if not found:
        print("No matching expenses found.")


def handle_choice(choice, expenses):

    if choice == "1":
        amount = input("Enter Amount: ")
        amount = validate_amount(amount)

        if amount is None:
            return

        category = input("Enter Category: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        description = input("Enter Description: ")

        expenses.append(Expense(amount, category, date, description))
        print("Expense added successfully.")

    elif choice == "2":
        show_all_expenses(expenses)

    elif choice == "3":
        category_summary(expenses)

    elif choice == "4":
        monthly_report(expenses)

    elif choice == "5":
        search_expense(expenses)

    elif choice == "6":
        backup_data()

    elif choice == "7":
        return "exit"

    else:
        print("Invalid choice. Please try again.")
