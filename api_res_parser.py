import json

class APIResponse:
    def __init__(self, data):
        self.raw_data = data
        self.parsed_data = self.parse_data()
    
    def parse_data(self):
        try:
            return json.loads(self.raw_data)
        except json.JSONDecodeError:
            return None
    
    def get_value(self, key_path):
        """Get nested value using dot notation"""
        current = self.parsed_data
        for key in key_path.split('.'):
            if isinstance(current, dict):
                current = current.get(key)
            else:
                return None
        return current

# Test with sample data
sample_response = '''
{
    "user": {
        "id": 1,
        "name": "John Doe",
        "address": {
            "street": "123 Main St",
            "city": "Boston"
        }
    },
    "status": "active"
}
'''

response = APIResponse(sample_response)
print(response.get_value("user.name"))  # John Doe
print(response.get_value("user.address.city"))  # Boston
