

from LibraryManager import LibraryManager

def main():
    # Create an instance of LibraryManager
    library = LibraryManager()

    # Sample data for demonstration
    books_data = [
        {"title": "Introduction to Operating Systems", "author": "John Doe", "publisher": "Tech Press", "volume": "1", "year": 2021, "isbn": "978-1234567890"},
        {"title": "Data Structures and Algorithms", "author": "Jane Smith", "publisher": "Code Books", "volume": "2", "year": 2022, "isbn": "978-0987654321"},
        {"title": "Machine Learning with Python", "author": "Alice Johnson", "publisher": "Data Science Publishers", "volume": "3", "year": 2023, "isbn": "978-1122334455"},
        # Add 22 more books similarly
    ]

    # Add books to the library
    for book in books_data:
        library.add_book(book['title'], book['author'], book['publisher'], book['volume'], book['year'], book['isbn'])

    # List all books
    print("All books in the library:")
    print(library.list_books())
    print()

    # Retrieve and display details of a book
    isbn_to_check = "978-1234567890"
    print(f"Details of book with ISBN {isbn_to_check}:")
    print(library.get_book_details(isbn_to_check))
    print()

    # Search for books by title or author
    search_term = "Machine Learning"
    print(f"Search results for '{search_term}':")
    print(library.search_books(search_term))
    print()

    # Update a book
    isbn_to_update = "978-1234567890"
    print(f"Updating book with ISBN {isbn_to_update}:")
    library.update_book(isbn_to_update, title="Advanced Operating Systems")
    print(library.get_book_details(isbn_to_update))
    print()

    # Check if a book is available
    isbn_to_check_availability = "978-0987654321"
    print(f"Is book with ISBN {isbn_to_check_availability} available?")
    print(library.is_book_available(isbn_to_check_availability))
    print()

    # Remove a book
    isbn_to_remove = "978-1122334455"
    print(f"Removing book with ISBN {isbn_to_remove}:")
    library.remove_book(isbn_to_remove)
    print(library.list_books())

if __name__ == "__main__":
    main()
