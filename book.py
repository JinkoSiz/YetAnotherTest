class Book:
    """
    Класс для представления книги в библиотеке.
    """
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализация книги.
        
        :param id: Уникальный идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param status: Статус книги (по умолчанию "в наличии").
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        """
        Возвращает строковое представление книги.
        
        :return: Строка, представляющая книгу.
        """
        return f"{self.id}: {self.title} by {self.author}, {self.year} - {self.status}"
