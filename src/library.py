import json
from typing import List

from src.book import Book


class Library:
    """
    Класс для управления библиотекой.
    """
    # Константа для хранения данных
    STORAGE_FILE = "src/storage.json"

    def __init__(self):
        self.books: List[Book] = self._load_books()

    def _load_books(self) -> List[Book]:
        """
        Загружает книги из файла.
        """
        try:
            with open(self.STORAGE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_books(self):
        """
        Сохраняет книги в файл.
        """
        with open(self.STORAGE_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """
        Добавляет книгу в библиотеку.
        """
        book_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self._save_books()
        print(f"Книга '{title}' успешно добавлена с ID {book_id}.")

    def delete_book(self, book_id: int):
        """
        Удаляет книгу по ID.
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self._save_books()
                print(f"Книга с ID {book_id} успешно удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query: str, field: str = "title") -> List[Book]:
        """
        Ищет книги по заданному полю.
        """
        return [book for book in self.books if query.lower() in str(getattr(book, field, "")).lower()]

    def display_books(self):
        """
        Отображает список всех книг.
        """
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def update_status(self, book_id: int, status_input: str):
        """
        Изменяет статус книги. Можно вводить статус словом или цифрой.
        """
        status_map = {"1": "в наличии", "2": "выдана"}

        # Проверяем, является ли ввод цифрой, иначе оставляем как есть
        status = status_map.get(status_input, status_input)

        # Проверяем, является ли статус корректным
        if status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Введите 'в наличии', 'выдана' или их номера (1, 2).")
            return

        # Изменяем статус книги по ID и сохраняем изменения статуса
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self._save_books()
                print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
                return

        print(f"Книга с ID {book_id} не найдена.")
