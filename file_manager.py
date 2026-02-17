import csv
import shutil
from expense import Expense

FILE_PATH = "data/expenses.csv"


def save_expenses(expenses):
    with open(FILE_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        
        for expense in expenses:
            writer.writerow(expense.to_list())


def load_expenses():
    expenses = []

    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = Expense(
                    float(row["Amount"]),   # ⭐ Important fix
                    row["Category"],
                    row["Date"],
                    row["Description"]
                )
                expenses.append(expense)

    except FileNotFoundError:
        pass

    return expenses


def backup_data():
    shutil.copy(FILE_PATH, "data/backup_expenses.csv")
    print("Backup created successfully.")
