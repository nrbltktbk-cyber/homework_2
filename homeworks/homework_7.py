import sqlite3

def create_table():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()


# функция добавления книг
def insert_books():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    books = [
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 5),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 470, 3),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 430, 4),
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 2),
        ("Гарри Поттер", "Дж. К. Роулинг", 1997, "Фэнтези", 320, 10),
        ("Хоббит", "Дж. Р. Р. Толкин", 1937, "Фэнтези", 310, 6),
        ("Алхимик", "Пауло Коэльо", 1988, "Философия", 208, 7),
        ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 8),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 480, 4),
        ("Шантарам", "Грегори Дэвид Робертс", 2003, "Роман", 936, 3),
    ]

    cursor.executemany("""
        INSERT INTO books 
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана и книги добавлены успешно")
