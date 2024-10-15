import sqlite3

# Initialize the database tables if they don't exist
def initialize_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
        isbn TEXT PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        quantity INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Borrowers (
        membership_id TEXT PRIMARY KEY,
        name TEXT,
        contact TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS BorrowedBooks (
        membership_id TEXT,
        isbn TEXT,
        due_date TEXT,
        FOREIGN KEY(membership_id) REFERENCES Borrowers(membership_id),
        FOREIGN KEY(isbn) REFERENCES Books(isbn)
    )''')

    conn.commit()
    conn.close()

# Connection to the database using sqlite
def get_db_connection():
    return sqlite3.connect('library.db')
