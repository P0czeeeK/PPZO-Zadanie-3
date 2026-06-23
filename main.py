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

    def __str__(self):
        return f"Id {self.id}, title {self.title}, author {self.author}, is available {self._is_available}"

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

    def __str__(self):
        return f"Id {self.id}, imie {self.name}"

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

    def what_user_id(self):
        return len(self.user_list)
    
    def what_book_id(self):
        return len(self.book_list)
    
    def check_user_list(self):
        for i in self.user_list:
            print(i)

    def check_book_list(self):
        for i in self.book_list:
            print(i)

    def available_books(self):
        return self.book_list

    def add_user(self, user):
        self.user_list.append(user)

    def add_book(self, item):
        self.book_list.append(item)

    def borrow_item(self, user_id, item_id):
        pass

    def return_item(self, user_id, item_id):
        pass

    def find_item_by_id(self, id):
        pass

    def find_user_by_id(self, id):
        pass

def admin(name, password):
    if(name != "admin" and password != "admin"):
        print("Błąd! Użytkownik nieznany")
    else:
        print("Witaj adminie!")
        while True:
            print("Co chciałbyś zrobić?")
            x = int(input("1 - Dodaj użytkownika\n2 - Dodaj książkę\n3 - Dodaj ebooka\n4 - Wypożyczyć książkę użytkownikowi\n5 - Użytkownik zwrócił książkę\n6 - Wypisz listę użytkowników\n7 - Wypisz listę książek\n0 - Wyloguj\n"))
            match x:
                case 1:
                    user_name = input("Podaj imie użytkownika\n")
                    id = library.what_user_id()
                    user = User(id, user_name)
                    library.add_user(user)
                case 2:
                    book_author = input("Podaj autora\n")
                    book_title = input("Podaj tytuł książki\n")
                    id = library.what_book_id()
                    book = Book(id, book_title, book_author)
                    library.add_book(book)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    library.check_user_list()
                case 7:
                    library.check_book_list()
                case 0:
                    break
                case _:
                    print("Nie ma takiego wyboru")

def guest():
    print("Witaj gościu, aktualne książki które można wypożyczyć: ")
    print(Library.available_books())

def main():
    print("*******************Biblioteka*******************")
    while True:
        print("Co chciałbyś zrobić?")
        x = int(input("1 - Zaloguj\n2 - Kontunuuj jako gość\n0 - Wyjście\n"))
        match x:
            case 1:
                name = input("Podaj login: ")
                password = input("Podaj hasło: ")
                admin(name, password)
            case 2:
                guest()
            case 0:
                print("Żegnaj!")
                break
            case _:
                print("Brak takiej opcji")

library = Library()
main()