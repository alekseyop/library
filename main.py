from src.library import Library


def main():
    """
    Основная функция программы.
    """

    # Создаем экземпляр класса Library
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":  # добавить книгу
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)

        elif choice == "2":  # удалить книгу
            book_id = int(input("Введите ID книги для удаления: "))
            library.delete_book(book_id)

        elif choice == "3":  # искать книгу
            query = input("Введите запрос для поиска: ")
            field = input("Искать по (title/author/year): ").lower()
            results = library.search_books(query, field)

            if results:
                for book in results:
                    print(
                        f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == "4":  # показать все книги
            library.display_books()

        elif choice == "5":  # изменить статус книги
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, status)

        elif choice == "0":  # выход из программы
            print("Выход из программы.")
            exit()

        else:  # возвращаемся в меню
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
