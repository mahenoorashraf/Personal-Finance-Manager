# Import functions for menu display and handling user choices
from menu import show_menu, handle_choice 
# Import functions to load and save expenses from CSV
from file_manager import load_expenses, save_expenses

def main():
    """
    Main function to run the Personal Finance Manager CLI.
    
    - Loads existing expenses from CSV
    - Displays menu and handles user input in a loop
    - Saves data and exits when user chooses to quit
    """
    # Load existing expenses from CSV file (returns a list of Expense objects)
    expenses = load_expenses()

    # Infinite loop to keep showing the menu until user exits
    while True:
        # Display the main menu
        show_menu()

        # Get user's choice from input
        choice = input("Enter your choice: ")

        # If user chooses "7", save all expenses and exit
        if choice == "7":
            save_expenses(expenses)  # Save data to CSV
            print("Data saved. Exiting...")
            break  # Exit the loop and program

        # Handle other menu choices like adding/viewing/searching expenses
        handle_choice(choice, expenses)


# Run the main function when this file is executed directly
if __name__ == "__main__":
    main()
