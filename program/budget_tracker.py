import json
import os
from datetime import datetime, date

DATA_FILE = "transactions.json"


def load_transactions(filepath: str) -> list:
    """
    Reads transaction data from a JSON file and returns it as a list.
    Args:
        filepath: Path to the data file (.json)
    Returns:
        List of transaction dictionaries
    Example:
        >>> load_transactions("transactions.json")
        [{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}]
    Edge cases handled:
        - File not found -> returns empty list and prints "No past data found. Starting fresh."
        - Corrupted file -> returns empty list and prints warning
    """
    if not os.path.exists(filepath):
        print("No past data found. Starting fresh.")
        return []
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data.get("transactions", [])
    except (json.JSONDecodeError, IOError):
        print("Data file is corrupted. Starting fresh.")
        return []


def save_transactions(transactions: list, filepath: str) -> None:
    """
    Writes transaction data to a JSON file for persistence.
    Args:
        transactions: List of transaction dictionaries to save
        filepath: Path to the data file (.json)
    Returns:
        None
    Example:
        >>> save_transactions([{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}], "transactions.json")
    Edge cases handled:
        - Empty list -> writes file with empty transactions
        - File path invalid -> creates file if it doesn't exist
    """
    balance = calculate_balance(transactions)
    data = {
        "transactions": transactions,
        "total_balance": balance
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def calculate_balance(transactions: list) -> float:
    """
    Calculates the current total balance from all transactions.
    Args:
        transactions: List of transaction dictionaries
    Returns:
        Total balance as a float (income - expenses)
    Example:
        >>> calculate_balance([{"type": "income", "amount": 50.0}, {"type": "expense", "amount": 12.5}])
        37.5
    Edge cases handled:
        - Empty list -> returns 0.0
        - Only expenses -> returns negative number
    """
    balance = 0.0
    for t in transactions:
        if t["type"] == "income":
            balance += t["amount"]
        else:
            balance -= t["amount"]
    return balance


def add_transaction(transactions: list) -> None:
    """
    Prompts the user to add a new transaction (income or expense).
    Args:
        transactions: The list of transaction dictionaries to append to
    Returns:
        None (modifies transactions list in place)
    Edge cases handled:
        - Invalid type input -> rejects and re-prompts
        - Non-numeric amount -> rejects: "Please enter a valid number for amount."
        - Negative or zero amount -> rejects: "Please enter a positive amount."
        - Empty purpose -> rejects: "Purpose cannot be empty. Try again."
    """
    print("\n--- Add New Transaction ---")

    while True:
        trans_type = input("Is this income or expense? ").strip().lower()
        if trans_type in ("income", "expense"):
            break
        print("Please enter 'income' or 'expense'.")

    while True:
        amount_str = input("Enter amount: ").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    while True:
        purpose = input("Enter purpose: ").strip()
        if purpose:
            break
        print("Purpose cannot be empty. Try again.")

    today = date.today().isoformat()
    transaction = {
        "type": trans_type,
        "amount": amount,
        "purpose": purpose,
        "date": today
    }
    transactions.append(transaction)
    save_transactions(transactions, DATA_FILE)
    print("Transaction saved successfully!")


def view_all_transactions(transactions: list) -> None:
    """
    Displays all recorded transactions with type, amount, purpose, and date.
    Args:
        transactions: List of transaction dictionaries
    Returns:
        None (prints to console)
    Example:
        >>> view_all_transactions([{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}])
    Edge cases handled:
        - Empty list -> prints "No transaction history yet. Please add a transaction first."
        - Many transactions -> lists each one line-by-line
    """
    print("\n--- All Transactions ---")
    if not transactions:
        print("No transaction history yet. Please add a transaction first.")
        return

    for t in transactions:
        type_label = t["type"].capitalize()
        print(f"{type_label} | {t['amount']} | {t['purpose']} | {t['date']}")

    balance = calculate_balance(transactions)
    print(f"\nTotal Balance: {balance}")


def check_total_balance(transactions: list) -> None:
    """
    Displays the current total balance.
    Args:
        transactions: List of transaction dictionaries
    Returns:
        None (prints to console)
    Edge cases handled:
        - Empty list -> prints balance as 0.0
    """
    print("\n--- Total Balance ---")
    balance = calculate_balance(transactions)
    print(f"Your current balance is: {balance}")


def calculate_daily_limit(balance: float) -> float:
    """
    Calculates how much money the user can spend per day for the rest of the month.
    Args:
        balance: Current total available money, accepts positive or negative float numbers
    Returns:
        Daily spending limit as a float number
    Example:
        >>> calculate_daily_limit(100)
        5.0
    Edge cases handled:
        - Negative balance -> returns 0.0
        - Last day of month -> returns full remaining balance
    """
    if balance <= 0:
        return 0.0

    today = date.today()
    # Get last day of current month
    if today.month == 12:
        last_day = date(today.year + 1, 1, 1)
    else:
        last_day = date(today.year, today.month + 1, 1)

    days_left = (last_day - today).days
    if days_left <= 0:
        return balance

    return round(balance / days_left, 2)


def show_daily_limit(transactions: list) -> None:
    """
    Displays the daily spending limit for the rest of the month.
    Args:
        transactions: List of transaction dictionaries
    Returns:
        None (prints to console)
    Edge cases handled:
        - Zero or negative balance -> prints "You have no available spending money right now."
        - Last day of month -> shows full remaining balance
    """
    print("\n--- Daily Spending Limit ---")
    balance = calculate_balance(transactions)

    if balance <= 0:
        print("You have no available spending money right now.")
        return

    daily = calculate_daily_limit(balance)
    print(f"You can spend {daily} per day for the rest of the month.")


def show_menu() -> None:
    """
    Displays the main menu to the user.
    """
    print()
    print("=" * 36)
    print("      WELCOME TO 存点钱吧。。。")
    print("=" * 36)
    print("1. Add a new transaction")
    print("2. View all transactions")
    print("3. Check total balance")
    print("4. Calculate daily spending limit")
    print("5. Exit")
    print()


def main():
    """
    Main function that runs the budget tracker app loop.
    """
    transactions = load_transactions(DATA_FILE)

    while True:
        show_menu()
        choice = input("What would you like to do? (1-5): ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_all_transactions(transactions)
        elif choice == "3":
            check_total_balance(transactions)
        elif choice == "4":
            show_daily_limit(transactions)
        elif choice == "5":
            print("\nThanks for using 存点钱吧。。。! Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
