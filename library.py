"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []
book_counter = 1  

def add_book(title, author, **kwargs):
    """
    Add a new book into the library with flexible details.
    Returns: "Book {book_title} added successfully!"
    """
    global book_counter
    book = {
        "id": book_counter,
        "title": title,
        "author": author,
        "available": True
    }
    # Add any extra details like genre, year, etc.
    book.update(kwargs)

    library.append(book)
    book_counter += 1
    return f"Book '{title}' added successfully!"


def search_books(search_param):
    """
    Search for books by keyword (title or author).
    Returns a list of matching books.
    """
    search_param = search_param.lower()
    results = []
    for book in library:
        if search_param in book["title"].lower() or search_param in book["author"].lower():
            results.append(book)
    return results


def borrow_book(book_id):
    """
    Borrow a book if available.
    Returns:
        "You borrowed {book_title}" if available
        "Book {book_title} not available" if already borrowed
    """
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' not available."
    return "Book ID not found!"

print("===============Example usage===============")
print(add_book("1984", "George Orwell", genre="Dystopian"))
print(add_book("To Kill a Mockingbird", "Harper Lee", year=1960))
print(add_book("Python Programming", "John Doe", year=2022))

print("\nSearch Results for 'python':")
print(search_books("python"))

print("\nBorrowing a book:")
print(borrow_book(3))
print(borrow_book(3))  

