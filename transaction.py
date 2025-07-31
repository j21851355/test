class Transaction:
    def __init__(self, amount: float, transaction_type: str, description: str = ""):
        self.transaction_id = str(uuid.uuid4())
        self.amount = amount
        self.type = transaction_type
        self.description = description
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ${self.amount:.2f} - {self.description}"
