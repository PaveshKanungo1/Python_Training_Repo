def search_book(catalog, attribute, search_term):
    return [book for book in catalog if search_term in book[attribute].lower()]

def display_results(books):
    if books:
        print("\nYour Book:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Category: {book['category']}")
    else:
        print("No matching result")

def main():
    catalog = [
        {'title': '1984', 'author': 'George Orwell', 'category': 'Dystopian'},
        {'title': 'A Brief History of Time', 'author': 'Stephen Hawking', 'category': 'Science'},
        {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'category': 'Fiction'},
        {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'category': 'Adventure'}
    ]

    while True:
        print("\nLibrary Catalog Search:")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Category")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            search_term = input("Enter the book title to search: ").strip().lower()
            results = search_book(catalog, 'title', search_term)
            display_results(results)
        elif choice == 2:
            search_term = input("Enter the author's name to search: ").strip().lower()
            results = search_book(catalog, 'author', search_term)
            display_results(results)
        elif choice == 3:
            search_term = input("Enter the category's name to search: ").strip().lower()
            results = search_book(catalog, 'category', search_term)
            display_results(results)
        elif choice == 4:
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()