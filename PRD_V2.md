# Final Project PRD V2

## Part 1: Project Identity (1-2 paragraphs)

"存点钱吧。。。" is a budget tracker that helps high school students manage their income and expenses by recording transactions and calculating daily spending limits. The target user is high school students with pocket money or 零花钱 who want to track their money and avoid overspending. I picked this project because I really want to manage my own money better and use some Python skills to solve my real life problem.

**Required:**

- [x] Project name: 存点钱吧。。。 (Save Some Money...)
- [x] One-sentence pitch: "存点钱吧。。。 is a CLI budget tracker that helps high school students manage their pocket money by recording income and expenses, calculating daily spending limits, and storing transaction history locally."
- [x] Target user: High school students (ages 14-18) with pocket money, allowance, or part-time job income who want to develop good financial habits and avoid overspending.
- [x] Why this project: I picked this because I really want to manage my own money better and use Python skills to solve a real-life problem.

---

## Part 2: Feature Scope — The "Must-Have" List

**You must have EXACTLY 3-5 core features. No more, no less.**

### Feature 1: Add a Transaction

**What it does:** Lets the user record income or expense entries with an amount and spending purpose.

**Why it matters:** This is the core input feature that lets users log all money coming in and going out.

**User flow:**
1. App shows menu → user selects "Add transaction"
2. Income or expense? → user types: "income"
3. Enter amount: → user types: "50"
4. Enter purpose: → user types: "monthly allowance"
5. "Transaction saved"

**Edge cases:**
- User enters text instead of number for amount → App rejects: "Please enter a valid number for amount."
- User enters empty purpose → App rejects: "Purpose cannot be empty. Try again."

### Feature 2: View All Transactions

**What it does:** Displays every recorded income and expense with details, plus the current total balance.

**Why it matters:** Lets users review their spending history and see exactly where their money goes.

**User flow:**
1. App shows menu, user selects "View all transactions"
2. App prints all transactions with type, amount, purpose, and date
3. App shows final line: "Current total balance: [number]"

**Edge cases:**
- If no transactions have been added → App shows: "No transaction history yet. Please add a transaction first."
- If the user has many transactions → App lists each one clearly line-by-line without errors.

### Feature 3: Calculate Daily Spending Limit

**What it does:** Shows how much money the user can safely spend each day for the rest of the current month.

**Why it matters:** Helps users budget and avoid running out of money before month-end.

**User flow:**
1. App shows menu → user selects "Calculate daily spending limit"
2. App calculates remaining balance ÷ days left in month
3. App shows: "Your daily spending limit is: [number]"

**Edge cases:**
- If user has zero or negative balance → App shows: "You have no available spending money right now."
- If it is the last day of the month → App shows full remaining balance as daily limit.

---

## Part 3: Data Architecture

**You must define ALL data your app stores.**

### 3a: Data Structure (JSON or Python dict)

```json
{
    "transactions": [
        {
            "type": "income",
            "amount": 50.0,
            "purpose": "allowance",
            "date": "2025-05-20"
        },
        {
            "type": "expense",
            "amount": 12.5,
            "purpose": "bubble tea",
            "date": "2025-05-20"
        }
    ],
    "total_balance": 37.5
}
```

### 3b: Data Flow Diagram

- **Where does data come FROM?** User input when adding transactions.
- **Where does data get STORED?** Stored in a text file on the computer.
- **When does data get READ?** When the app starts up.
- **When does data get WRITTEN?** Right after every transaction is added or updated.

---

## Part 4: Function Specifications

**You must define EVERY function your app will have.**

```python
def add_transaction(trans_type: str, amount: float, purpose: str) -> dict:
    """
    Creates a new transaction and adds it to the transaction list.
    Args:
        trans_type: Either "income" or "expense"
        amount: Positive number representing the transaction amount
        purpose: Non-empty string describing the transaction purpose
    Returns:
        The newly created transaction dict with date included.
    Example:
        >>> add_transaction("income", 50.0, "allowance")
        {"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}
    Edge cases handled:
        - Empty purpose → raises ValueError: "Purpose cannot be empty"
        - Negative or zero amount → raises ValueError: "Please enter a positive amount"
    """

def view_all_transactions(transactions: list) -> str:
    """
    Displays all recorded transactions with type, amount, purpose, and date.
    Args:
        transactions: List of transaction dictionaries
    Returns:
        Formatted string of all transactions with total balance.
    Example:
        >>> view_all_transactions([{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}])
        "Income | 50.0 | allowance | 2025-05-20\nTotal Balance: 50.0"
    Edge cases handled:
        - Empty list → returns "No transaction history yet. Please add a transaction first."
        - Many transactions → lists each one line-by-line
    """

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
        - Negative balance → returns 0.0
        - Last day of month → returns full remaining balance
    """

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
        - Empty list → returns 0.0
        - Only expenses → returns negative number
    """

def load_transactions(filepath: str) -> list:
    """
    Reads transaction data from a file and returns it as a list.
    Args:
        filepath: Path to the data file (.txt or .csv)
    Returns:
        List of transaction dictionaries
    Example:
        >>> load_transactions("transactions.txt")
        [{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}]
    Edge cases handled:
        - File not found → returns empty list and prints "No past data found. Starting fresh."
        - Corrupted file → returns empty list and prints warning
    """

def save_transactions(transactions: list, filepath: str) -> None:
    """
    Writes transaction data to a file for persistence.
    Args:
        transactions: List of transaction dictionaries to save
        filepath: Path to the data file (.txt or .csv)
    Returns:
        None
    Example:
        >>> save_transactions([{"type": "income", "amount": 50.0, "purpose": "allowance", "date": "2025-05-20"}], "transactions.txt")
    Edge cases handled:
        - Empty list → writes empty file
        - File path invalid → creates file if it doesn't exist
    """
```

**You must have at least 5 functions. Each must have:**

- [x] Function signature (name, parameters, return type)
- [x] Docstring with description
- [x] Args documented
- [x] Return value documented
- [x] At least 2 edge cases handled

---

## Part 5: User Interface & Interaction Design

### 5a: Main Menu

```
====================================
      WELCOME TO 存点钱吧。。。
====================================
1. Add a new transaction
2. View all transactions
3. Check total balance
4. Calculate daily spending limit
5. Exit

What would you like to do? (1-5):
```

### 5b: Screen-by-Screen Flow

**Option 1 — Add a new transaction:**
```
--- Add New Transaction ---
Is this income or expense?
income
Enter amount:
50
Enter purpose:
allowance
Transaction saved successfully!
```

**Option 2 — View all transactions:**
```
--- All Transactions ---
Income | 50.0 | allowance | 2025-05-20
Expense | 12.5 | bubble tea | 2025-05-20
Total Balance: 37.5
```

**Option 3 — Check total balance:**
```
--- Total Balance ---
Your current balance is: 37.5
```

**Option 4 — Calculate daily spending limit:**
```
--- Daily Spending Limit ---
You can spend 2.5 per day for the rest of the month
```

**Option 5 — Exit:**
```
Thanks for using 存点钱吧。。。! Goodbye!
```

---

## Part 6: Error Handling & Edge Cases

| # | Error Scenario | App Response |
|---|---------------|-------------|
| 1 | User types letters when a number is needed | "Please enter a valid number." |
| 2 | User enters empty purpose for transaction | "Purpose cannot be empty. Please try again." |
| 3 | Data file is missing on startup | "No past data found. Starting fresh." |
| 4 | User enters amount less than zero | "Please enter a positive amount." |
| 5 | User chooses a menu number that does not exist | "Please choose a number from 1 to 5." |

---

## Part 7: Testing Plan

**How will you know your app works?** Define at least 3 test cases:

- **Test 1:** Adding an income transaction and checking if balance increases correctly.
- **Test 2:** Adding an expense transaction and checking if balance decreases correctly.
- **Test 3:** Daily limit calculation with different balances to ensure correct math.
