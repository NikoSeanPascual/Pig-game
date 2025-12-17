class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: ₱{amount}")
            print(f"Successfully deposited ₱{amount}.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: ₱{amount}")
            print(f"You withdrew ₱{amount}.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"\n--- Current Balance: ₱{self.balance} ---")

    def show_history(self):
        print("\n--- Transaction History ---")
        if not self.history:
            print("No transactions yet.")
        for item in self.history:
            print(item)


def main():
    try:
        start_bal = float(input("Enter starting balance: "))
    except ValueError:
        print("Invalid input. Starting with ₱0.")
        start_bal = 0

    account = BankAccount(start_bal)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit 💸")
        print("2. Withdraw 💰")
        print("3. Show Balance 💳")
        print("4. Transaction History 💲")
        print("5. Exit")

        choice = input("Select an option (1-5): ")
        if choice == '1':
            try:
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '2':
            try:
                amt = float(input("Enter withdrawal amount: "))
                account.withdraw(amt)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == '3':
            account.show_balance()

        elif choice == '4':
            account.show_history()

        elif choice == '5':
            print("Thank you for using our bank. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()