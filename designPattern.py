# Example: Singleton Pattern
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.value = 0
        
# Test Singleton
s1 = Singleton()
s2 = Singleton()
print(f"Are objects same? {s1 is s2}")
