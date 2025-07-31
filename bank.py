class Bank:
    def __init__(self, name: str):
        self.name = name
        self.customers: Dict[str, Customer] = {}
        self.accounts: Dict[str, BankAccount] = {}
    
    def create_customer(self, name: str, email: str) -> Customer:
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer
    
    def create_account(self, customer: Customer, account_type: str = "Savings") -> BankAccount:
        account_number = str(uuid.uuid4())
        account = BankAccount(account_number, account_type)
        customer.add_account(account)
        self.accounts[account_number] = account
        return account
    
    def get_customer(self, customer_id: str) -> Customer:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return self.customers[customer_id]
    
    def get_account(self, account_number: str) -> BankAccount:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]
