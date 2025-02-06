

class Book:
    page_material = 'бумага'
    text_availability = True

    def __init__(self, book_title, author, page_count, isbn, reserved=False):
        self.book_title = book_title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved


    def book_to_string(self):
        reserved_status = 'зарезервирована' if self.reserved else 'незарезервирована'
        return f'Название: {self.book_title}, Автор: {self.author}, страниц: {self.page_count}, ' \
               f'материал: {Book.page_material}, Статус: {reserved_status}'

# экземпляры
book1 = Book("Идиот", "Достаевский", 500, "9788420608051", reserved=False)
book2 = Book("Преступение и наказание", "Достаевский", 1000, "9788420741468", reserved=False)
book3 = Book("Война и мир", "Толстой", 1500, "9780393042375", reserved=False)
book4 = Book("Отцы и дети", "Толстой", 330, "9785042023149", reserved=False)
book5 = Book("Пиковая дама", "Пушкин", 250, "9785002148592", reserved=True)

for book in [book1, book2, book3, book4, book5]:
    print(book.book_to_string())

class Textbook(Book):
    def __init__(self, book_title, author, page_count, isbn, school_grade,
                 school_class, exercise, reserved=False):
        super().__init__(book_title, author, page_count, isbn, reserved)
        self.school_grade = school_grade
        self.school_class = school_class
        self.exercise = exercise


    def textbook_to_string(self):
        reserved_status = 'зарезервирована' if self.reserved else 'незарезервирована'
        return f'Название: {self.book_title}, Автор: {self.author}, страниц: {self.page_count},' \
               f'предмет: {self.school_class} класс: {self.school_grade}, статус: {reserved_status}'

# экземпляры
textbook1 = Textbook("Математика", "Иванов", 100, "1234567890123", "Математика", 9, True, reserved=True)
textbook2 = Textbook("История", "Петров", 200, "1234567890124", "История", 10, True, reserved=False)
textbook3 = Textbook("География", "Сидоров", 300, "1234567890125", "География", 11, True, reserved=False)

textbooks = [textbook1, textbook2, textbook3]

for textbook in textbooks:
    print(textbook.textbook_to_string())
