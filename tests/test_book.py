# test_book.py
import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_get_info(self):
        # Test 1: Verifică dacă metoda get_info returnează informațiile corecte pentru o carte.
        # Creare obiect Book cu titlul "Harry Potter" și autorul "J.K. Rowling".
        book = Book("Harry Potter", "J.K. Rowling")

        # Apelare metoda get_info() pentru obținerea informațiilor despre carte.
        rezultat = book.get_info()

        # Verificare utilizând self.assertEqual că rezultatul este cel așteptat.
        self.assertEqual(rezultat, "Harry Potter - J.K. Rowling")
        print('Test 1: Afiseaza informatiile despre carte:', rezultat)

        # Test 2: Verifică dacă metoda get_info funcționează corect pentru o altă carte.
        another_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
        rezultat_another = another_book.get_info()
        self.assertEqual(rezultat_another, "The Great Gatsby - F. Scott Fitzgerald")
        print('Test 2: Afiseaza informatiile despre alta carte:', rezultat_another)

    #@unittest.skip
    def test_update_stock(self):
        # Testează actualizarea corectă a stocului cărții.
        book = Book("Dune", "Frank Herbert", stock=4)

        # Adaugă 4 exemplare la stoc.
        book.update_stock(4)
        self.assertEqual(book.stock, 8, "Actualizare incorectă a stocului după adăugarea a 4 exemplare.")
        print('Test 3: Adaugă 4 exemplare la stoc și verifică noul stoc:', book.stock)

        # Scoate 2 exemplare din stoc.
        book.update_stock(-2)
        self.assertEqual(book.stock, 6, "Actualizare incorectă a stocului după scoaterea a 2 exemplare.")
        print('Test 4: Scoate 2 exemplare din stoc și verifică noul stoc:', book.stock)

        # Asigură-te că stocul nu devine negativ.
        book.update_stock(-6)
        self.assertEqual(book.stock, 0, "Stocul ar trebui să fie 0 după ce s-au scos 6 exemplare.")
        print('Test 5: Asigură-te că stocul nu devine negativ și verifică noul stoc:', book.stock)



