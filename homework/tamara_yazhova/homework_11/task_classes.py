class Book:
    text = True
    material_of_page = "бумага"

    def __init__(self, name, author, page_count, isbn, reserve=False):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserve = reserve

    def reserved_book(self):
        if self.reserve:
            return (f"Название: {self.name}, Автор: {self.author}, "
                    f"страниц: {self.page_count}, материал: {self.material_of_page}, зарезервирована")
        else:
            return (f"Название: {self.name}, Автор: {self.author}, "
                    f"страниц: {self.page_count}, материал: {self.material_of_page}")


class Textbook(Book):
    def __init__(self, name, author, page_count, isbn, subject, group, task=True, reserve = False):
        super().__init__(name, author, page_count, isbn, reserve)
        self.subject = subject
        self.group = group
        self.task = task

    def reserved_text_book(self):
        if self.reserve:
            return (f"Название: {self.name}, Автор: {self.author}, "
                    f"страниц: {self.page_count}, предмет: {self.subject}, класс: {self.group}, зарезервирована")
        else:
            return (f"Название: {self.name}, Автор: {self.author}, "
                    f"страниц: {self.page_count}, предмет: {self.subject}, класс: {self.group}")

book_1 = Book("Идиот", "Достоевский", 500, 687698)
book_2 = Book("Фауст", "Гете", 456, 573485)
book_3 = Book("Сто лет одиночества", "Маркес", 645, 563789)
book_4 = Book("Герой нашего времени", "Лермонтов", 256, 545123)
book_5 = Book("Мастер и Маргарита", "Булгаков", 567, 658456, reserve = True)

books = [book_1, book_2, book_3, book_4, book_5]

for book in books:
    print(book.reserved_book())

text_book_1 = Textbook(
    "Алгебра", "Иванов", 200, 567587,
    "Математика", 9, True
)
text_book_2 = Textbook(
    "Химия 8", "Петрова", 98, 567587, "Химия", 8, True
)
text_book_3 = Textbook(
    "Русская литература 7", "Сидоров", 150, 567587,
    "Литература", 7, False, reserve=True
)
text_book_4 = Textbook(
    "Геометрия", "Борисова",78, 567587, "Математика", 7, True
)

textbooks = [text_book_1, text_book_2, text_book_3, text_book_4]

for textbook in textbooks:
    print(textbook.reserved_text_book())
