library = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "borrowed": False},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "borrowed": False},
    {"title": "1984", "author": "George Orwell", "borrowed": True},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "borrowed": False},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "borrowed": True},
    {"title": "Moby Dick", "author": "Herman Melville", "borrowed": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "borrowed": True},
    {"title": "War and Peace", "author": "Leo Tolstoy", "borrowed": False},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "borrowed": False},
    {"title": "Brave New World", "author": "Aldous Huxley", "borrowed": True},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "borrowed": False},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "borrowed": True},
    {"title": "Charlotte's Web", "author": "E.B. White", "borrowed": False},
    {"title": "Frankenstein", "author": "Mary Shelley", "borrowed": True},
    {"title": "The Odyssey", "author": "Homer", "borrowed": False},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "borrowed": True},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "borrowed": False},
    {"title": "Little Women", "author": "Louisa May Alcott", "borrowed": False},
    {"title": "Animal Farm", "author": "George Orwell", "borrowed": True},
    {"title": "The Alchemist", "author": "Paulo Coelho", "borrowed": False},
]

def view_library():
    print("\nLibrary Books:\n")
    for book in library:
        if book['borrowed']:
            av = 'no'
        else:
            av = 'yes'
        print(f"Title: {book['title']}\n"
              f"Author: {book['author']}\n"
              f"Available: {av}\n")

def borrow_book(title):
    book_found = False
    book = dict() 
    for _book in library:
        if _book['title'] == title:
            book_found = True
            book = _book
            break
    if book_found:
        if book['borrowed']:
            print("Sorry this book is borrowed, you can not borrow it.")
        else:
            book['borrowed'] = True
            print(f'You have successfully borrowed {title}')
    else:
        print(f'Sorry we do not have {title}')
        
def add_book(book):
    library.append(book)

def remove_book(title):
    book_found = False
    book = dict() 
    for _book in library:
        if _book['title'] == title:
            book_found = True
            book = _book
            break
    if book_found:
        library.remove(book)
        print(f'You have successfully removed {title} from the library')
    else:
        print(f'Sorry we do not have {title}, so you can\'t remove it')

def display_menu():
    print("\nLibrary Management System")
    print("1. View Library")
    print("2. Borrow a Book")
    print("3. Add a Book")
    print("4. Remove a Book")
    print("Q. Quit")
    return input("\nEnter your choice: ")

def main():
    while True:
        choice = display_menu()
        
        if choice.lower() == 'q':
            print("\nThank you for using the Library Management System. Goodbye!")
            break    
        if choice == '1':
            view_library()
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            borrow_book(title)
        elif choice == '3':
            title = input("Enter the title of the book: ")
            author = input("Enter the author's name: ")
            add_book({"title": title, "author": author, "borrowed": False})
        elif choice == '4':
            title = input("Enter the title of the book to remove: ")
            remove_book(title)
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

