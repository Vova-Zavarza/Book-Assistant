import shelve


class Book:
    def __init__(self, name):
        self.name = name
        self.pages = int(input('Dies ist ein neues Buch. Wie viel Seiten hat dieses Buch?: '))
        self.user_page = int(input('Wie viel Seiten hast du gelesen?: '))
        self.day = int(input('Wie viele Tage möchtest du dieses Buch lesen?: '))
        self.count = count = (self.pages - self.user_page) // self.day
        print(f'Das Buch {name} entsteht!'.upper())

    def tagesrate(self):
        return f'Du müsst {self.count} Seiten pro Tag lesen.'

    def new_result(self):
        page = int(input('Auf welcher Seite bist du?: '))
        self.user_page = page

    def __str__(self):
        return f"---Name: {self.name}\n---Seiten: {self.pages}\n---Dein Fortschirt: {self.user_page}"


book_base = shelve.open(r'database/book_base') # open storage when save all information about books

print("HELPER BOOK READER".center(32))
user = input("Enter your book: ").rstrip()

if user in book_base:           # wenn dieses Buch alt ist
    real_book = book_base[user]
else:                           # wenn dieses Buch neu ist
    real_book = Book(name=user)
    book_base[user] = real_book


while True:                                                                                 # Hauptschliefe
    command_dict = {"fortschrit":  real_book, "neuer fortschrit": real_book.new_result}
    command = input(">: ").lower().rstrip()
    if command == 'stop':
        book_base[real_book.name] = real_book
        book_base.close()
        break
    elif command in command_dict:
        if command == 'neuer fortschrit':
            command_dict[command]()
        else:
            print(command_dict[command])

