# BookStore-Management

This Python code provides a simple e-bookstore database management system using SQLite3. It allows you to:

Create and maintain a book database with book ID, title, author, and quantity.
Add new books with unique IDs and quantities.
Update existing book quantities.
Delete books from the database.
Search for books by title or author using a keyword search.
Requirements:

Python 3.x (with sqlite3 module installed)
Getting Started

Installation: Ensure you have Python 3 installed. If you don't have the sqlite3 module, install it using pip install sqlite3.
Running the Script: Save the code as a Python file (e.g., ebookstore_manager.py) and run it from your terminal using python ebookstore_manager.py.
Database Structure

The script creates an SQLite3 database named ebookstore.db with a table called book containing these columns:

id (INTEGER PRIMARY KEY): Unique identifier for each book (auto-increments on insertion).
title (TEXT): Title of the book.
author (TEXT): Author's name.
qty (INTEGER): Available quantity of the book.
Using the Script

The script presents a menu when launched:

Menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit

Enter your choice: 
1. Enter book: Enter details (ID, title, author, quantity) to add a new book.
2. Update book: Enter the book ID to update and the new quantity.
3. Delete book: Enter the book ID to remove from the database.
4. Search books: Enter a keyword (title or author) to search for matching books.
0. Exit: Close the program.
Functionality

Data Validation: The script attempts to handle basic user input validation (e.g., ensuring integers for book ID and quantity).
Error Handling: The script incorporates basic error handling to gracefully handle potential database errors (e.g., duplicate book IDs).
Disclaimer

This script is for educational purposes only. For production environments, consider further security measures and enhancements:

