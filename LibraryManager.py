# LibraryManager.py

class LibraryManager:
    def __init__(self):
        """Initializes an empty library."""
        self.books = {}

    def add_book(self, title, author, publisher, volume, year, isbn):
        """Adds a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }
            print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        """Removes a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def get_book_details(self, isbn):
        """Retrieves and displays the details of a book using its ISBN."""
        if isbn in self.books:
            return self.books[isbn]
        else:
            print(f"Book with ISBN {isbn} not found.")
            return None

    def search_books(self, search_term):
        """Searches for books by title or author."""
        results = {}
        for isbn, details in self.books.items():
            if search_term.lower() in details['title'].lower() or search_term.lower() in details['author'].lower():
                results[isbn] = details
        return results

    def list_books(self):
        """Lists all books currently in the library."""
        return self.books

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        """Updates the details of an existing book."""
        if isbn in self.books:
            if title:
                self.books[isbn]['title'] = title
            if author:
                self.books[isbn]['author'] = author
            if publisher:
                self.books[isbn]['publisher'] = publisher
            if volume:
                self.books[isbn]['volume'] = volume
            if year:
                self.books[isbn]['year'] = year
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def is_book_available(self, isbn):
        """Checks if a book is available in the library by its ISBN."""
        return isbn in self.books
