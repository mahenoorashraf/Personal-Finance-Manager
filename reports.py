from collections import defaultdict


def show_all_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(expense)


def category_summary(expenses):
    summary = defaultdict(float)

    for expense in expenses:
        summary[expense.category] += expense.amount

    print("\nCategory Wise Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")


def monthly_report(expenses):
    monthly = defaultdict(float)

    for expense in expenses:
        month = expense.date[:7]   # YYYY-MM
        monthly[month] += expense.amount

    print("\nMonthly Report:")
    for month, total in monthly.items():
        print(f"{month}: ₹{total}")
