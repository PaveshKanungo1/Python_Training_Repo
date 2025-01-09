
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        print(f"Book's title is {self.title} and Book's author is {self.author}") 

def display_operations():
    print("::Library::")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. List all Books")
    print("5. Exit")

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    new_book = Book(title, author)
    library.append(new_book)
    print(f"Book:: Title: {title} and Author: {author} added successfully")

def remove_book(library):
    title = input("Enter the name of the book to be removed: ")
    for book in library:
        if book.title.lower == title.lower:
            library.remove(book)
            print(f"Book:: Title: {title} is removed successfully")
            return
    print(f"Book is not found in the library")

def search_book(library):
    title = input("Enter the name of the book: ")
    for book in library:
        if book.title.lower == title.lower:
            print(f"Found Book: {title}")
            return
    print(f"Book is not found in the library")

def list_books(library):
    print(f"Books in library: ")
    for book in library:
        print(f"{book}")

def main():
    library = []
    while True:
        display_operations()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book(library)
        elif choice == 2:
            remove_book(library)
        elif choice == 3:
            search_book(library)
        elif choice == 4:
            list_books(library)
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose from the give options.")
    
if __name__ == "__main__":
    main()


