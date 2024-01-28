# test_library.py
import unittest
from book import Book
from library import Library

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        # Creare obiect Library.
        library = Library()

        # Creare obiect Book cu titlul "The Hobbit" și autorul "J.R.R. Tolkien".
        book = Book("The Hobbit", "J.R.R. Tolkien", stock=2)
        book1 = Book("The Silmarillion", "J.R.R. Tolkien", stock=1)
        book2 = Book("To Kill a Mockingbird", "Harper Lee", stock=6)

        # Adăugare cărții în bibliotecă utilizând metoda add_book().
        library.add_book(book)
        library.add_book(book1)
        library.add_book(book2)

        # Obținere lista de cărți din bibliotecă.
        rezultat = library.get_books()

        # Afișare rezultat utilizând print.
        print('Lista de cărți după adăugare:', rezultat)

        # Verificare utilizând self.assertEqual că rezultatul este cel așteptat (o listă conținând obiectul Book creat anterior).
        #self.assertEqual(rezultat, [book, book1, book2])
        self.assertEqual([str(book) for book in rezultat], [str(book) for book in [book, book1, book2]])



    #@unittest.skip  # Decorator pentru a nu rula testul
    def test_remove_book(self):
        # Testează eliminarea corectă a cărților din bibliotecă.
        library = Library()
        book3 = Book("1984", "George Orwell", stock=1)
        book4 = Book("The Catcher in the Rye", "J.D. Salinger", stock=1)

        library.add_book(book3)
        library.add_book(book4)

        # Afisare lista de cărți înainte de eliminare.
        print('Lista de cărți înainte de eliminare:', [str(book) for book in library.get_books()])

        # Elimină o carte din bibliotecă.
        library.remove_books(book3)
        rezultat = library.get_books()
        self.assertEqual([str(book) for book in rezultat], [str(book4)])

        # Afisare lista de cărți după eliminare.
        print('Lista de cărți după eliminare:', [str(book) for book in rezultat])


















