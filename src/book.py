from typing import Dict


class Book:
    """
    Класс для представления книги.
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

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
