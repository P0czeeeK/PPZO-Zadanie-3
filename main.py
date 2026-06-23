import datetime as dt

class Item:

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def borrow(self):
        pass

    def return_item(self):
        pass

class Book(Item):
    def __init__(self, id, title, author, is_available = True):
        super().__init__(id, title, author)
        self._is_available = is_available

    def borrow(self):
        self._is_available = False

    def return_item(self):
        self._is_available = True

class EBook(Item):
    def __init__(self, id, title, author, file_size, download_limit):
        super().__init__(id, title, author)
        self.file_size = file_size
        self.download_limit = download_limit

    def borrow(self):
        if self.download_limit <= 0:
            return False
        
        if self.download_limit > 0:
            self.download_limit -= 1

    def return_item(self):
        pass

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._borrowed_items = []

    def borrow_item(self, item):
        pass

    def return_item(self, item):
        pass

    def list_loans(self):
        return self._borrowed_items
    
class Loan:
    def __init__(self, loan_id, user, item, loan_date, return_date = None):
        self.loan_id = loan_id
        self.user = user
        self.item = item
        self.loan_date = loan_date
        self.return_date = return_date

    def close(self):
        self.return_date = dt.datetime.now()

class Library:
    def __init__(self, user_list = None, book_list = None, loan_list = None):
        self.user_list = user_list or []
        self.book_list = book_list or []
        self.loan_list = loan_list or []

    def add_user(self, user):
        pass

    def add_item(self, item):
        pass

    def borrow_item(self, user_id, item_id):
        pass

    def return_item(self, user_id, item_id):
        pass

    def find_item_by_id(self, id):
        pass

    def find_user_by_id(self, id):
        pass