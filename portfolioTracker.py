class PortfolioTracker:
    def __init__(self):
        self.holdings = {}
        self.transactions = []

    def add_transaction(self, symbol, shares, price, transaction_type):
        self.transactions.append({
            'date': datetime.now(),
            'symbol': symbol,
            'shares': shares,
            'price': price,
            'type': transaction_type
        })
        
        if symbol not in self.holdings:
            self.holdings[symbol] = {'shares': 0, 'cost_basis': 0}
            
        if transaction_type == 'buy':
            self.holdings[symbol]['shares'] += shares
            self.holdings[symbol]['cost_basis'] += (shares * price)
        else:
            self.holdings[symbol]['shares'] -= shares

    def get_portfolio_value(self, current_prices):
        total_value = 0
        for symbol, holding in self.holdings.items():
            if symbol in current_prices:
                value = holding['shares'] * current_prices[symbol]
                total_value += value
        return total_value

    def get_performance(self, current_prices):
        performance = {}
        for symbol, holding in self.holdings.items():
            if symbol in current_prices and holding['shares'] > 0:
                current_value = holding['shares'] * current_prices[symbol]
                cost_basis = holding['cost_basis']
                gain_loss = current_value - cost_basis
                performance[symbol] = {
                    'shares': holding['shares'],
                    'cost_basis': cost_basis,
                    'current_value': current_value,
                    'gain_loss': gain_loss,
                    'return_percentage': (gain_loss / cost_basis) * 100
                }
        return performance
