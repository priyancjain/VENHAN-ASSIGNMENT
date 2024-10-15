from library_db import get_db_connection, initialize_db
from logging_config import log_info, log_error
import sqlite3
# Book class to handle book management
class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Books (isbn, title, author, genre, quantity) VALUES (?, ?, ?, ?, ?)', 
                           (self.isbn, self.title, self.author, self.genre, self.quantity))
            conn.commit()
            log_info(f"Book added: {self.title} (ISBN: {self.isbn})")
        except sqlite3.IntegrityError:
            log_error(f"Error: Book with ISBN {self.isbn} already exists.")
            print(f"Error: Book with ISBN {self.isbn} already exists.")
        finally:
            conn.close()

    @staticmethod
    def update(isbn, title=None, author=None, genre=None, quantity=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Books WHERE isbn = ?', (isbn,))
        book = cursor.fetchone()

        if book:
            new_title = title if title else book[1]
            new_author = author if author else book[2]
            new_genre = genre if genre else book[3]
            new_quantity = quantity if quantity is not None else book[4]

            cursor.execute('UPDATE Books SET title = ?, author = ?, genre = ?, quantity = ? WHERE isbn = ?',
                           (new_title, new_author, new_genre, new_quantity, isbn))
            conn.commit()
            log_info(f"Book updated: {isbn}")
            print(f"Book '{isbn}' updated successfully!")
        else:
            log_error(f"Error: Book with ISBN {isbn} not found.")
            print(f"Error: Book with ISBN {isbn} not found. Please enter correct information.")
        conn.close()

    @staticmethod
    def delete(isbn):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE isbn = ?', (isbn,))
        if cursor.rowcount > 0:
            conn.commit()
            log_info(f"Book removed: {isbn}")
            print(f"Book '{isbn}' removed successfully!")
        else:
            log_error(f"Error: Book with ISBN {isbn} not found.")
            print(f"Error: Book with ISBN {isbn} not found. Please enter correct information.")
        conn.close()

    @staticmethod
    def search(title=None, author=None, genre=None):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM Books WHERE 1=1"
        params = []
        if title:
            query += " AND title LIKE ?"
            params.append(f"%{title}%")
        if author:
            query += " AND author LIKE ?"
            params.append(f"%{author}%")
        if genre:
            query += " AND genre LIKE ?"
            params.append(f"%{genre}%")

        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

        if results:
            return results
        else:
            print("No books found. Please enter correct information.")
            return []
        
    @staticmethod
    def check_availability(isbn):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT quantity FROM Books WHERE isbn = ?', (isbn,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return result[0]  # Return the quantity available
        else:
            print(f"Book with ISBN {isbn} not found. Please enter correct information.")
            return None

# Borrower class to manage borrower details
class Borrower:
    def __init__(self, membership_id, name, contact):
        self.membership_id = membership_id
        self.name = name
        self.contact = contact

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO Borrowers (membership_id, name, contact) VALUES (?, ?, ?)', 
                           (self.membership_id, self.name, self.contact))
            conn.commit()
            log_info(f"Borrower added: {self.name} (Membership ID: {self.membership_id})")
        except sqlite3.IntegrityError:
            log_error(f"Error: Borrower with ID {self.membership_id} already exists.")
            print(f"Error: Borrower with ID {self.membership_id} already exists.")
        finally:
            conn.close()

    @staticmethod
    def update(membership_id, name=None, contact=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Borrowers WHERE membership_id = ?', (membership_id,))
        borrower = cursor.fetchone()

        if borrower:
            new_name = name if name else borrower[1]
            new_contact = contact if contact else borrower[2]

            cursor.execute('UPDATE Borrowers SET name = ?, contact = ? WHERE membership_id = ?',
                           (new_name, new_contact, membership_id))
            conn.commit()
            log_info(f"Borrower updated: {membership_id}")
            print(f"Borrower '{membership_id}' updated successfully!")
        else:
            log_error(f"Error: Borrower with ID {membership_id} not found.")
            print(f"Error: Borrower with ID {membership_id} not found. Please enter correct information.")
        conn.close()

    @staticmethod
    def delete(membership_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Borrowers WHERE membership_id = ?', (membership_id,))
        if cursor.rowcount > 0:
            conn.commit()
            log_info(f"Borrower removed: {membership_id}")
            print(f"Borrower '{membership_id}' removed successfully!")
        else:
            log_error(f"Error: Borrower with ID {membership_id} not found.")
            print(f"Error: Borrower with ID {membership_id} not found. Please enter correct information.")
        conn.close()

# Borrowing management class
class Borrowing:
    @staticmethod
    def borrow_book(membership_id, isbn, due_date):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the book is available
        cursor.execute('SELECT quantity FROM Books WHERE isbn = ? AND quantity > 0', (isbn,))
        book = cursor.fetchone()

        if book:
            # Check if borrower exists
            cursor.execute('SELECT * FROM Borrowers WHERE membership_id = ?', (membership_id,))
            borrower = cursor.fetchone()

            if borrower:
                cursor.execute('INSERT INTO BorrowedBooks (membership_id, isbn, due_date) VALUES (?, ?, ?)', 
                               (membership_id, isbn, due_date))
                cursor.execute('UPDATE Books SET quantity = quantity - 1 WHERE isbn = ?', (isbn,))
                conn.commit()
                log_info(f"Book borrowed: {isbn} by {membership_id} (Due: {due_date})")
                print(f"Book '{isbn}' borrowed by '{membership_id}' successfully!")
            else:
                log_error("Borrower not found!")
                print("Borrower not found!")
        else:
            log_error("Book is not available!")
            print("Book is not available!")
        conn.close()

    @staticmethod
    def return_book(membership_id, isbn):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM BorrowedBooks WHERE membership_id = ? AND isbn = ?', (membership_id, isbn))
        borrowed = cursor.fetchone()

        if borrowed:
            cursor.execute('DELETE FROM BorrowedBooks WHERE membership_id = ? AND isbn = ?', (membership_id, isbn))
            cursor.execute('UPDATE Books SET quantity = quantity + 1 WHERE isbn = ?', (isbn,))
            conn.commit()
            log_info(f"Book returned: {isbn} by {membership_id}")
            print(f"Book '{isbn}' returned by '{membership_id}' successfully!")
        else:
            log_error(f"No record of book '{isbn}' being borrowed by '{membership_id}'.")
            print(f"No record of book '{isbn}' being borrowed by '{membership_id}'.")
        conn.close()
