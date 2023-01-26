import json


def load_books_from_json():
    """
    Загружает книжки из файла
    """
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
    return books


def save_books_to_json(books):
    """
    Сохраняет список словарей в json-файл
    """

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False)

