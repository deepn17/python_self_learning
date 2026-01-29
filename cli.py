print("Welcome to the Financial Planner")
print("================================")

# GLOBAL DATA STORE
transactions = []

def add_transaction(date, t_type, amount, category):
    """Adds a new transaction dictionary to the list"""
    new_transaction = {
        "date": date,
        "type": t_type,
        "amount": amount,
        "category": category
    }
    transactions.append(new_transaction)
    print(f"✅ Added: {t_type} of ₹{amount} for {category}")

def view_transactions():
    """Prints all transactions in readable format"""
    print("\n--- Transaction History ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for index, t in enumerate(transactions):
            print(f"{index + 1}. {t['date']} | {t['type']} | {t['amount']} | {t['category']}")
    print("-------------------------\n")

def get_summary():
    """Calculates total income, total expense, and current balance."""
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expense

    print("\n--- Financial Summary---")
    print(f"💰 Total Income: ₹{total_income:.2f}")
    print(f"💸 Total Expense: ₹{total_expense:.2f}")
    print(f"🏦 Net Balance: ₹{balance}")
    print("-------------------------\n")

def main():
    while True:
        print("1. Add Transactions")
        print("2. View History")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Select your option (1-4): ")
        if choice == '1':
            date = input("Enter the date (DD-MM-YYYY): ")
            t_type = input("Enter Type (income/expense): ")
            amount = float(input("Enter amount: ₹"))
            category = input("Enter Category (Food, Salary, etc.): ")
            add_transaction(date, t_type, amount, category)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            get_summary()
        elif choice == '4':
            print('Exiting... Goodbye')
            break
        else:
            print("Invalid Selection, try again")


if __name__ == '__main__':
    main()