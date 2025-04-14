import json
import os

LIBRARY_FILE = "library.txt"

# Load library from file if it exists
if os.path.exists(LIBRARY_FILE):
    with open(LIBRARY_FILE, "r") as file:
        try:
            library = json.load(file)
        except json.JSONDecodeError:
            library = []
else:
    library = []

def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    save_library()
    print("Book added successfully!\n")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        matches = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        matches = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice.\n")
        return

    if matches:
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
        print()
    else:
        print("No matching books found.\n")

def display_all_books():
    if not library:
        print("Your library is empty.\n")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    print()

def display_statistics():
    total_books = len(library)
    if total_books == 0:
        percentage_read = 0
    else:
        read_books = sum(1 for book in library if book["read"])
        percentage_read = (read_books / total_books) * 100

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%\n")

def main_menu():
    while True:
        print("""
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
        """)
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
