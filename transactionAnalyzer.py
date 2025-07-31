from datetime import datetime
import pandas as pd

class BankTransactionAnalyzer:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount, transaction_type):
        """Add a new transaction to the list"""
        transaction = {
            'date': datetime.strptime(date, '%Y-%m-%d'),
            'description': description,
            'amount': float(amount),
            'type': transaction_type  # 'credit' or 'debit'
        }
        self.transactions.append(transaction)

    def get_balance(self):
        """Calculate current balance"""
        balance = 0
        for transaction in self.transactions:
            if transaction['type'] == 'credit':
                balance += transaction['amount']
            else:
                balance -= transaction['amount']
        return round(balance, 2)

    def get_spending_by_category(self):
        """Analyze spending by category"""
        categories = {}
        for transaction in self.transactions:
            if transaction['type'] == 'debit':
                category = transaction['description'].split('-')[0].strip()
                if category in categories:
                    categories[category] += transaction['amount']
                else:
                    categories[category] = transaction['amount']
        return categories

    def get_monthly_summary(self):
        """Generate monthly income and expense summary"""
        df = pd.DataFrame(self.transactions)
        df['month'] = df['date'].dt.strftime('%Y-%m')
        
        monthly_summary = {}
        for month in df['month'].unique():
            month_data = df[df['month'] == month]
            income = month_data[month_data['type'] == 'credit']['amount'].sum()
            expenses = month_data[month_data['type'] == 'debit']['amount'].sum()
            
            monthly_summary[month] = {
                'income': round(income, 2),
                'expenses': round(expenses, 2),
                'net': round(income - expenses, 2)
            }
        return monthly_summary

    def get_largest_transactions(self, n=5):
        """Get the n largest transactions"""
        sorted_transactions = sorted(self.transactions, 
                                  key=lambda x: x['amount'], 
                                  reverse=True)
        return sorted_transactions[:n]

# Example usage
if __name__ == "__main__":
    analyzer = BankTransactionAnalyzer()

    # Add sample transactions
    analyzer.add_transaction('2023-01-01', 'Salary', 5000, 'credit')
    analyzer.add_transaction('2023-01-02', 'Groceries-Food', 100, 'debit')
    analyzer.add_transaction('2023-01-03', 'Rent-Housing', 1200, 'debit')
    analyzer.add_transaction('2023-01-04', 'Utilities-Bills', 150, 'debit')
    analyzer.add_transaction('2023-02-01', 'Salary', 5000, 'credit')
    analyzer.add_transaction('2023-02-05', 'Shopping-Clothes', 200, 'debit')

    # Get current balance
    print("\nCurrent Balance:", analyzer.get_balance())

    # Get spending by category
    print("\nSpending by Category:")
    categories = analyzer.get_spending_by_category()
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

    # Get monthly summary
    print("\nMonthly Summary:")
    monthly_summary = analyzer.get_monthly_summary()
    for month, data in monthly_summary.items():
        print(f"\nMonth: {month}")
        print(f"Income: ${data['income']}")
        print(f"Expenses: ${data['expenses']}")
        print(f"Net: ${data['net']}")

    # Get largest transactions
    print("\nLargest Transactions:")
    largest_transactions = analyzer.get_largest_transactions(3)
    for transaction in largest_transactions:
        print(f"{transaction['date'].strftime('%Y-%m-%d')} - {transaction['description']}: ${transaction['amount']}")
