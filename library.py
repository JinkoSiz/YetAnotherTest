import json
from book import Book

class Library:
    """
    Класс для управления коллекцией книг в библиотеке.
    """
    def __init__(self, data_file: str):
        """
        Инициализация библиотеки.

        :param data_file: Путь к файлу с данными библиотеки.
        """
        self.data_file = data_file
        self.books = self.load_books()
        self.next_id = max((book.id for book in self.books), default=0) + 1

    def load_books(self):
        """
        Загрузка книг из файла.

        :return: Список книг.
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                return [Book(**book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        """
        Сохранение книг в файл.
        """
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """
        Добавление новой книги в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        new_book = Book(self.next_id, title, author, year)
        self.books.append(new_book)
        self.next_id += 1
        self.save_books()
        print(f"Book '{title}' added with ID {new_book.id}.")

    def remove_book(self, book_id: int):
        """
        Удаление книги из библиотеки по ID.

        :param book_id: Уникальный идентификатор книги.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Book ID {book_id} removed.")
        else:
            print(f"Book ID {book_id} not found.")

    def find_book_by_id(self, book_id: int):
        """
        Поиск книги по ID.

        :param book_id: Уникальный идентификатор книги.
        :return: Найденная книга или None.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, **kwargs):
        """
        Поиск книг по заданным критериям.

        :param kwargs: Критерии поиска (title, author, year).
        :return: Список найденных книг.
        """
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if str(getattr(book, key)).lower() == str(value).lower()]
        return results

    def display_books(self):
        """
        Отображение всех книг в библиотеке.
        """
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def update_status(self, book_id: int, status: str):
        """
        Обновление статуса книги по ID.

        :param book_id: Уникальный идентификатор книги.
        :param status: Новый статус книги.
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            print(f"Book ID {book_id} status updated to '{status}'.")
        else:
            print(f"Book ID {book_id} not found.")
