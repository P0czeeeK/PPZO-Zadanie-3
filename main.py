class Item:

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def borrow():
        pass

    def return_item():
        pass

class Book(Item):
    def __init__(self, id, title, author, is_available):
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
        self.download_limit - 1

    def return_item():
        pass