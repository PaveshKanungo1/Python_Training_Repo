class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    def __lt__(self, other):
        return self.title < other.title

    def __eq__(self, other):
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)
    

def main():
    books = [
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949)
    ]
    books.sort()
    print("Books sorted by title:")
    for book in books:
        print(book)

    books.sort(key=lambda b: b.author)
    print("\nBooks sorted by author:")
    for book in books:
        print(book)

    books.sort(key=lambda b: b.year)
    print("\nBooks sorted by year:")
    for book in books:
        print(book)