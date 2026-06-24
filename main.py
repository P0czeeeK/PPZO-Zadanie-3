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
    
    def user_view(self):
        return f"Tytuł: {self.title}, Autor: {self.author}"

    def borrow(self):
        self._is_available = False

    def return_item(self):
        self._is_available = True

class EBook(Item):
    def __init__(self, id, title, author, file_size, download_limit):
        super().__init__(id, title, author)
        self.file_size = file_size
        self.download_limit = download_limit

    def __str__(self):
        return f"Id {self.id}, Title {self.title}, Author: {self.author}, File size {self.file_size}, Download limit {self.download_limit}"
    
    def user_view(self):
        return f"Tytuł: {self.title}, Autor: {self.author}, File size {self.file_size}"

    def borrow(self):
        if self.download_limit <= 0:
            return False
        
        if self.download_limit > 0:
            self.download_limit -= 1
            return True

    def return_item(self):
        pass

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._borrowed_items = []

    def __str__(self):
        if not self._borrowed_items:
            return f"Id {self.id}, imie {self.name}"
        else:
            titles = ", ".join(item.title for item in self._borrowed_items)
            return f"Id {self.id}, imie {self.name}, książki: {titles}"



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

    def __str__(self):
        return f"Id {self.loan_id}, User {self.user.name}, item {self.item.title}, loan date {self.loan_date}, return date {self.return_date}"

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

    def check_loan_list(self):
        for i in self.loan_list:
            print(i)

    def available_books(self):
        return self.book_list

    def add_user(self, user):
        self.user_list.append(user)

    def add_book(self, item):
        self.book_list.append(item)

    def borrow_item(self, user_id, item_id):
        book = self.find_book_by_id(item_id)     
        user = self.find_user_by_id(user_id)

        if(user is None):
            print("Nie znaleziono użytkownika")
            return False

        if(book is None):
            print("Nie znaleziono książki")
            return False
        
        if not hasattr(book, "file_size"):
            if not book._is_available:
                print("Książka jest już wypożyczona")
                return False
            book.borrow()

        else:
            if(book.download_limit <=0 ):
                print("Ebook nie ma już dostępnych pobrań")
                return False
            book.borrow()

        loan_id = len(self.loan_list)
        loan = Loan(loan_id, user, book, dt.datetime.now())
        self.loan_list.append(loan)

        user._borrowed_items.append(book)
        print("Wypożyczono pomyślnie")
        return True

    def return_item(self, user_id, item_id):
        book = self.find_book_by_id(item_id)     
        user = self.find_user_by_id(user_id)

        if(user is None):
            print("Nie znaleziono użytkownika")
            return False

        if(book is None):
            print("Nie znaleziono książki")
            return False
        
        if not hasattr(book, "file_size"):
            if book._is_available:
                print("Książka nie jest wypożyczona")
                return False
            book.return_item()
        else:
            book.download_limit += 1

        for i in self.loan_list:
            if i.user == user and i.item == book and i.return_date is None:
                i.close()
                break

        user._borrowed_items_remove(book)
        print("Zwrócono książkę")
        return True

    def find_book_by_id(self, id):
        for i in self.book_list:
            if(id == i.id):
                return i

    def find_user_by_id(self, id):
        for i in self.user_list:
            if(id == i.id):
                return i


    def find_book_by_name(self, name):
        results = []
        for i in self.book_list:
            if(name.lower() in i.title.lower()):
                results.append(i)
        return results

    def find_user_by_name(self, name):
        results = []
        for i in self.user_list:
            if(name.lower() in i.name.lower()):
                results.append(i)
        return results

def admin(name, password):
    if(name.lower() != "admin" and password != "admin"):
        print("Błąd! Użytkownik nieznany")
    else:
        print("Witaj adminie!")
        while True:
            print("Co chciałbyś zrobić?")
            x = int(input("1 - Dodaj użytkownika\n2 - Dodaj książkę\n3 - Dodaj ebooka\n4 - Wypożyczyć książkę użytkownikowi\n5 - Użytkownik zwrócił książkę\n6 - Wypisz listę użytkowników\n7 - Wypisz listę książek\n8 - Wyszukaj użytkownika po imieniu\n9 - Wyszukaj książkę po nazwie\n10 - Wypisz listę wypożyczeń\n0 - Wyloguj\n"))
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
                    ebook_author = input("Podaj autora ebooka\n")
                    ebook_title = input("Podaj tytuł ebooka\n")
                    ebook_file_size = input("Podaj rozmiar ebooka\n")
                    ebook_download_limit = int(input("Podaj ilość dostępnych ebooków\n"))
                    id = library.what_book_id()
                    ebook = EBook(id, ebook_title, ebook_author, ebook_file_size, ebook_download_limit)
                    library.add_book(ebook)
                case 4:
                    user_id = int(input("Podaj id użytkownika który wypożycza książkę\n"))
                    book_id = int(input("Podaj id książki którą wypożycza\n"))
                    library.borrow_item(user_id, book_id)
                case 5:
                    user_id = int(input("Podaj id użytkownika który oddaje książkę\n"))
                    book_id = int(input("Podaj id książki którą oddaje\n"))
                    library.return_item(user_id, book_id)
                case 6:
                    library.check_user_list()
                case 7:
                    library.check_book_list()
                case 10:
                    library.check_loan_list()
                case 8:
                    user_name = input("Podaj imię które chcesz wyszukać\n")
                    results = library.find_user_by_name(user_name)

                    if results:
                        for i in results:
                            print(i)
                    else:
                        print("Nie znaleziono użytkownika o takim imieniu")
                case 9:
                    book_name = input("Podaj tutył który chcesz wyszukać\n")
                    results = library.find_book_by_name(book_name)

                    if results:
                        for i in results:
                            print(i)
                    else:
                        print("Nie znaleziono książki o takim tytule")
                case 0:
                    print("\nWylogowano")
                    break
                case _:
                    print("Nie ma takiego wyboru")

def guest():
    print("Witaj gościu, aktualne książki które można wypożyczyć: ")
    for book in library.book_list:
        if not hasattr(book, "file_size"):
            if(book._is_available == True):
                print(book.user_view())
    print("Aktualne Ebooki które można wypożyczyć: ")
    for book in library.book_list:
        if hasattr(book, "file_size"):
            if(book.download_limit > 0):
                print(book.user_view())

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