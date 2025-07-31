class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_statement(self):
        print(f"\nAccount: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

# Testing the BankAccount
account = BankAccount([REDACTED:BANK_ACCOUNT_NUMBER]")
account.deposit(1000)
account.withdraw(500)
account.deposit(300)
account.get_statement()
