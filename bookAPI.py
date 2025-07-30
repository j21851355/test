class BookAPI:
    def __init__(self):
        self.books = {}
        self.next_id = 1
        
    def add_book(self, title, author):
        book_id = self.next_id
        self.books[book_id] = {
            'id': book_id,
            'title': title,
            'author': author
        }
        self.next_id += 1
        return book_id
    
    def get_book(self, book_id):
        return self.books.get(book_id)
    
    def list_books(self):
        return list(self.books.values())

# Test API
api = BookAPI()
api.add_book("1984", "George Orwell")
api.add_book("Brave New World", "Aldous Huxley")
print(api.list_books())
