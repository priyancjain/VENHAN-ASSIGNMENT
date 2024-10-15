
# Library Management System

This is a Python-based library management system implemented using Object-Oriented Programming (OOP) principles. It allows users to manage books, borrowers, and the borrowing/returning process in a simplified library environment. The system uses SQLite as the database for persistence




## Features
- Book Management :
    - Add new books to the library with details like title, author, ISBN, genre, and quantity.
    - Update existing book information (e.g., title, author, quantity, genre) when necessary.
    - Remove books from the library when they are no longer available.
- Borrower Management :
    - Add new borrowers with details like name, contact information, and membership ID.
    - Update borrower information such as name and contact.
    - Remove borrowers from the system if necessary.
- Book Borrowing and Returning :
    - Borrow books by linking the borrower's membership ID to the book details.
    - Record the due date for each borrowed book.
    - Implement functionality for borrowers to return books, updating the database and restoring the quantity.
-  Book Search and Availability :
    - Provide a search feature that enables users to find books by title, author, or genre.
    - Show the availability status (number of copies) for each book in the search results.


## Installation



Prerequisites

Python 3.x (preferably 3.6 or higher)

SQLite (bundled with Python by default)
    
### Clone the repository
```bash
   git clone https://github.com/priyancjain/VENHAN-ASSIGNMENT.git

```

### Database Initialization
The system will automatically create the required SQLite database (library.db) and tables upon running the application. There's no need for manual setup.
## Usage

#### Running the application

To start the system, run the `menu.py` file:
```bash
python menu.py

```
This will bring up a menu where you can choose various operations such as adding books, borrowers, borrowing books, etc.

#### Menu Options
- Add Book: Adds a new book to the library database.
- Update Book: Updates existing book information.
- Remove Book: Removes a book from the library.
- Add Borrower: Adds a new borrower to the system.
- Update Borrower: Updates borrower information.
- Remove Borrower: Removes a borrower from the system.
- Borrow Book: Allows a borrower to borrow a book.
- Return Book: Allows a borrower to return a borrowed book.
- Search Books: Search for books by title, author, or genre.
 - Check Book Availability: Check how many copies of a book are available.
- Exit: Exits the application.

### Example
```bash
===== Library Management System =====
1. Add Book
2. Update Book
3. Remove Book
4. Add Borrower
5. Borrow Book
6. Return Book
7. Search Books
8. Check Book Availability
9. Exit
Choose an option (1-9):
```
## Project Structure
```bash
├── library_db.py       # Handles SQLite database setup
├── library_system.py   # Contains the OOP logic for book, borrower, and borrowing
├── menu.py             # The menu-driven interface to interact with the system
├── requirements.txt    # List of dependencies (if any)
├── library.db          # SQLite database (auto-generated when you run the app)
├── README.md           # Project documentation
├── logging_config.py   # it will contain all the logging activity
 ```
 ### Logging
 All actions, such as adding or updating books/borrowers, borrowing, and returning books, are logged into library.log. This helps track the activity within the system.

### Future Enhancements
- Overdue Handling: Implement logic to handle overdue books and charge fines.
- Web Interface: Create a web-based interface using Flask or Django.
- Report Generation: Generate reports for borrowed books, overdue books, etc.

