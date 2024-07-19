from library import Library

def main():
    library = Library('data.json')

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Update Book Status")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            try:
                year = int(input("Enter year: "))
                if year <= 0:
                    raise ValueError
                elif year >= 2024:
                    raise ValueError
                library.add_book(title, author, year)
            except ValueError:
                print("Invalid input for year. Please enter a positive number. The year shouldn't be more than 2024")
        elif choice == '2':
            try:
                book_id = int(input("Enter book ID to remove: "))
                library.remove_book(book_id)
            except ValueError:
                print("Invalid input for book ID. Please enter a number.")
        elif choice == '3':
            search_type = input("Search by (title/author/year): ").strip().lower()
            search_value = input(f"Enter {search_type}: ").strip()
            results = library.search_books(**{search_type: search_value})
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found matching the criteria.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            try:
                book_id = int(input("Enter book ID to update status: "))
                status = input("Enter new status ('в наличии'/'выдана'): ").strip().lower()
                if status in ['в наличии', 'выдана']:
                    library.update_status(book_id, status)
                else:
                    print("Invalid status. Please enter 'в наличии' or 'выдана'.")
            except ValueError:
                print("Invalid input for book ID. Please enter a number.")
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
