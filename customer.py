class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.accounts: Dict[str, BankAccount] = {}
        self.created_at = datetime.now()
        self.status = "Active"
    
    def add_account(self, account: BankAccount) -> bool:
        if account.account_number in self.accounts:
            raise ValueError("Account already exists")
        
        self.accounts[account.account_number] = account
        return True
    
    def get_account(self, account_number: str) -> BankAccount:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        
        return self.accounts[account_number]
    
    def get_total_balance(self) -> float:
        return sum(account.balance for account in self.accounts.values())
    
    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id}) - Total Balance: ${self.get_total_balance():.2f}"
