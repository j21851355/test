from datetime import datetime
import random

class Stock:
    def __init__(self, symbol, company_name, initial_price):
        self.symbol = symbol
        self.company_name = company_name
        self.current_price = initial_price
        self.price_history = [(datetime.now(), initial_price)]
        
    def update_price(self, new_price):
        self.current_price = new_price
        self.price_history.append((datetime.now(), new_price))
        
    def get_price_history(self):
        return self.price_history
