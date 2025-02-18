class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if the balance is sufficient."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₱{amount}. New balance: ₱{self.balance}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Displays the current balance."""
        print(f"Account balance: ₱{self.balance}")


account = BankAccount(account_number="702240658", owner="Sung Jinwoo", balance=1000)


account.deposit(500)
account.withdraw(200)
account.display_balance()
