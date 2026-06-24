# Biblioteka

## 1. Opis aplikacji
Aplikacja przedstawia prosty system biblioteczny umożliwiający zarządzanie użytkownikami, książkami, ebookami oraz wypożyczeniami. Administrator może dodawać użytkowników i pozycje do biblioteki, wypożyczać i przyjmować zwroty, a także przeglądać listy książek, użytkowników i wypożyczeń. Gość może przeglądać dostępne książki i ebooki. System wykorzystuje obiektowe podejście do modelowania elementów biblioteki.
## 2. Rzeczowniki z opisu (kandydaci na klasy)
Biblioteka
Użytkownik
Książka
Ebook
Przedmiot (Item)
Wypożyczenie (Loan)
Administrator
Gość
## 3. Klasy główne i ich odpowiedzialności
Item
Reprezentuje ogólny element biblioteczny. Przechowuje podstawowe dane wspólne dla książek i ebooków.
Book
Modeluje fizyczną książkę, którą można wypożyczyć i zwrócić. Przechowuje informację o dostępności.
EBook
Reprezentuje ebooka z limitem pobrań. Każde wypożyczenie zmniejsza limit.
User
Przechowuje dane użytkownika oraz listę wypożyczonych pozycji.
Loan
Rejestruje pojedyncze wypożyczenie: kto, co, kiedy i czy zwrócono.
Library
Zarządza użytkownikami, książkami, ebookami i wypożyczeniami. Odpowiada za logikę wypożyczania i zwrotów.
## 4. Właściwości klas
Item
id
title
author
Book
_is_available
EBook
file_size
download_limit
User
id
name
_borrowed_items
Loan
loan_id
user
item
loan_date
return_date
Library
user_list
book_list
loan_list
## 5. Metody klas
Item
borrow()
return_item()
Book
borrow() – ustawia dostępność na False
return_item() – ustawia dostępność na True
user_view() – uproszczony widok dla gościa
EBook
borrow() – zmniejsza limit pobrań
user_view()
User
borrow_item()
return_item()
list_loans()
Loan
close() – ustawia datę zwrotu
Library
add_user()
add_book()
borrow_item()
return_item()
find_user_by_id()
find_book_by_id()
find_user_by_name()
find_book_by_name()
check_user_list()
check_book_list()
check_loan_list()
## 6. Relacje między klasami
Library → User (kolekcja użytkowników)
Library → Book/EBook (kolekcja pozycji)
Library → Loan (kolekcja wypożyczeń)
Loan → User (agregacja)
Loan → Item (agregacja)
Book i EBook dziedziczą po Item
User → Item (lista wypożyczonych pozycji)
## 7. Implementacja i przykładowe uruchomienie
Kod zawiera pełną implementację klas oraz menu administratora i gościa.
Przykładowe działanie:
Admin dodaje użytkownika.
Admin dodaje książkę lub ebooka.
Admin wypożycza książkę użytkownikowi.
System tworzy obiekt Loan i dodaje go do listy wypożyczeń.
Użytkownik zwraca książkę – Loan zostaje zamknięty.
Gość może wyświetlić dostępne książki i ebooki.
## 8. Cztery zasady OOP w projekcie
Abstrakcja
Klasa Item reprezentuje wspólne cechy książek i ebooków.
Dziedziczenie
Book i EBook dziedziczą po Item.
Polimorfizm
Metody borrow() i return_item() działają inaczej dla Book i EBook.
Enkapsulacja
Pola takie jak _is_available czy _borrowed_items są ukryte i modyfikowane metodami.

### Login: admin
### Hasło: admin
