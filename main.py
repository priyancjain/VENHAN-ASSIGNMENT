from app import Book, Borrower, Borrowing
from library_db import initialize_db

# Menu-driven interface
def menu():
    initialize_db()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Add Borrower")
        print("5. Update Borrower")
        print("6. Remove Borrower")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Search Books")
        print("10. Check Book Availability")
        print("11. Exit")
        choice = input("Choose an option (1-11): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            genre = input("Enter genre: ")
            quantity = int(input("Enter quantity: "))
            book = Book(title, author, isbn, genre, quantity)
            book.save()

        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("New title (leave blank to skip): ")
            author = input("New author (leave blank to skip): ")
            genre = input("New genre (leave blank to skip): ")
            quantity = input("New quantity (leave blank to skip): ")
            quantity = int(quantity) if quantity else None
            Book.update(isbn, title, author, genre, quantity)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to remove: ")
            Book.delete(isbn)

        elif choice == '4':
            name = input("Enter borrower name: ")
            contact = input("Enter borrower contact: ")
            membership_id = input("Enter membership ID: ")
            borrower = Borrower(membership_id, name, contact)
            borrower.save()

        elif choice == '5':
            membership_id = input("Enter membership ID of the borrower to update: ")
            name = input("New name (leave blank to skip): ")
            contact = input("New contact (leave blank to skip): ")
            Borrower.update(membership_id, name, contact)

        elif choice == '6':
            membership_id = input("Enter membership ID to remove: ")
            Borrower.delete(membership_id)

        elif choice == '7':
            membership_id = input("Enter membership ID: ")
            isbn = input("Enter book ISBN: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            Borrowing.borrow_book(membership_id, isbn, due_date)

        elif choice == '8':
            membership_id = input("Enter membership ID: ")
            isbn = input("Enter book ISBN: ")
            Borrowing.return_book(membership_id, isbn)

        elif choice == '9':
            title = input("Enter book title (leave blank to skip): ")
            author = input("Enter author (leave blank to skip): ")
            genre = input("Enter genre (leave blank to skip): ")
            results = Book.search(title, author, genre)
            for book in results:
                print(book)

        elif choice == '10':
            isbn = input("Enter book ISBN: ")
            availability = Book.check_availability(isbn)
            print(f"Copies available: {availability}")

        elif choice == '11':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
