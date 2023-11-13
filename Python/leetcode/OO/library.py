'''
**Problem: Online Library Catalog System**

You are tasked with designing a simple online library catalog system. 
The system should allow users to search for books, check their availability, and borrow or return books. 
This system is intended to be a simplified version and should be designed to handle a moderate number of users and books efficiently.

**Requirements:**
1. **Book Database:** Create a database that stores information about books, including titles, authors, genres, publication dates, and availability status.
2. **User Management:** Implement user registration and login functionality. Users should be able to create accounts, log in, and view their borrowed books.
3. **Search and Browse:** Users should be able to search for books by title, author, or genre. They should also be able to browse books by genre.
4. **Borrowing and Returning:** Users should be able to borrow available books and return books they have borrowed. Ensure that books are properly marked as borrowed or available.
5. **Inventory Management:** Implement functionality for librarians to add new books to the catalog, mark books as borrowed or returned, and update book information.
6. **Availability Tracking:** The system should track the availability of books in real-time. Users should be notified if a book they want to borrow is unavailable.
7. **User Notifications:** Implement email notifications to remind users of due dates and notify them when a borrowed book is overdue.

**Implementation Constraints:**

- You have a 45-minute time limit for the initial design and coding phase.
- You can use Python and any libraries or frameworks of your choice.
- Focus on core functionality, and you can omit advanced features like fine-grained access control or payment processing.

Books
 Object
    - Title
    - Author
    - Genre
    - Publication Date
    - Availability Status

User
    - Name
    - phone
    - email
    - borrowed books
    - should be able to browse books by genre, title and author
    - book availability status management

Inventory [librarian]
    - add book
    - update book
    - update status
    - notify borrowers of books to return them

Notifications
    - When a book becomes available, notify all users of it
    - option to let a user express interest in a book

    

User
    - Librarian
    - Borrower

Book


'''

class User:

    def __init__(self, first_name, last_name, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
    
    def search_book(self, property):
        # There will be a list of books in our library. 
        # Searching can be done on one of three properties, we do that search on any of the properties, 
        # and also return if the book is available or not
        pass
    
    def currently_borrowed_books(self):
        pass

    def return_book(self, book):
        pass

    def get_history(self):
        pass


class Libriarian(User):

    def __init__(self, first_name, last_name, address, email, library):
        super().__init__(first_name, last_name, address, email)
        self.library = library

    def add_book(self, book):
        pass

    def update_book(self, book):
        # book can be updated based on the title, match title first and then update the rest of the properties
        pass

    def update_book_status(self, book, new_status):
        pass

    def list_borrowed_books(self, user = None):
        if not user:
            pass
        else:
            pass

    def notify_user(self, user, book = None):
        # generate a report saying the user was reminder to return their book
        pass

from enum import Enum

class BookStatus(Enum):
    AVAILABLE = 1
    ISSUED = 2
    OVERDUE = 3

class Genre(Enum):
    ACTION = 1
    MYSTERY = 2
    BIOGRAPHY = 3
    FICTION = 4

from collections import defaultdict
class Library:
    
    def __init__(self, name):
        self.name = name
        self.books_by_genre = defaultdict(list)
        self.books_by_author = defaultdict(list)
        self.books_by_title = defaultdict()

class Book:

    def __init__(self, title, author, genre, publication_date, status = BookStatus.AVAILABLE):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_Date = publication_date
        self.status = status


# create a librarian

librarian_bob = Libriarian("Bob", "Barley", "14016 Maricella Ln", "bobbarley@gmail.com", )


    

