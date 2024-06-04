# Import 
import sqlite3

# Create the database connection and cursor
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Create a table 'book' if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        qty INTEGER
    )
''')

# Populate the table with initial values
initial_books = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]

# Insert initial books into the table
cursor.executemany('''
    INSERT INTO book (id, title, author, qty)
    VALUES (?, ?, ?, ?)
''', initial_books)

# Commit changes to the database
conn.commit()

# Function to enter a new book into the database
def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    qty = int(input("Enter quantity: "))

    cursor.execute('''
        INSERT INTO book (id, title, author, qty)
        VALUES (?, ?, ?, ?)
    ''', (id, title, author, qty))

    conn.commit()
    print("Book added successfully!")

# Function to update the quantity of an existing book
def update_book():
    book_id = int(input("Enter book ID to update: "))
    new_qty = int(input("Enter new quantity: "))

    cursor.execute('''
        UPDATE book
        SET qty = ?
        WHERE id = ?
    ''', (new_qty, book_id))

    conn.commit()
    print("Book updated successfully!")

# Function to delete a book from the database
def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    cursor.execute('''
        DELETE FROM book
        WHERE id = ?
    ''', (book_id,))

    conn.commit()
    print("Book deleted successfully!")

# Function to search for books based on title or author
def search_books():
    keyword = input("Enter search keyword (title or author): ")
    cursor.execute('''
        SELECT * FROM book
        WHERE title LIKE ? OR author LIKE ?
    ''', ('%' + keyword + '%', '%' + keyword + '%'))

    books = cursor.fetchall()

    if not books:
        print("No matching books found.")
    else:
        for book in books:
            print(book)

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enter_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

# Close 
conn.close()
