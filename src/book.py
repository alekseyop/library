from typing import Dict


class Book:
    """
    Класс для представления книги.
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id  # id книги
        self.title = title  # название книги
        self.author = author  # автор книги
        self.year = year  # год издания
        self.status = status  # статус книги(в наличии, недоступна)

    def to_dict(self) -> Dict:
        """
        Конвертирует объект книги в словарь.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """
        Создает объект книги из словаря.
        """
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])
