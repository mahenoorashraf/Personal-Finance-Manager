class Expense:
    """
    Represents a single expense entry.
    
    Attributes:
        amount (float): Expense amount
        category (str): Expense category (Food, Transport, etc.)
        date (str): Date of the expense (YYYY-MM-DD)
        description (str): Short description of the expense
    """
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)  # Convert input amount to float for calculations
        self.category = category     # Store expense category
        self.date = date             # Store expense date
        self.description = description   # Store expense description

    def to_list(self):
        return [self.date, self.category, self.amount, self.description]

    def __str__(self):
        """
        Returns a formatted string representation of the expense.
        """
        return f"{self.date} | {self.category} | ₹{self.amount} | {self.description}"
        