# library.py

# Clasa Library reprezintă o structură care gestionează cărțile într-o bibliotecă
class Library:
    def __init__(self):
        # Pas 1: Initializează o bibliotecă nouă fără cărți.
        self.books = []

    def add_book(self, book):
        # Pas 2: Adaugă o carte la lista de cărți din bibliotecă.
        self.books.append(book)

    def get_books(self):
        # Pas 3: Returnează lista de cărți din bibliotecă.
        #return self.books
        return [str(book) for book in self.books]
        #return [book.get_display_info() for book in self.books]

    def remove_books(self, book):
        # Pas 4: Elimina o carte din biblioteca.
        if book in self.books:
            self.books.remove(book)
       #else:
           # print('Cartea nu exista in biblioteca!')

    def update_stock(self, book, quantity):
        # Actualizează stocul unei cărți în bibliotecă.
        if book in self.books:
            book.update_stock(quantity)
        else:
            print('Cartea nu exista in biblioteca!')




