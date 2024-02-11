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

        # Test 1: Verificare utilizând self.assertEqual că rezultatul este cel așteptat.
        self.assertEqual(rezultat, "Harry Potter - J.K. Rowling")
        print('Test 1: Afiseaza informatiile despre carte:', rezultat)

        # Test 2: Verifică dacă metoda get_info funcționează corect pentru o altă carte.
        another_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
        rezultat_another = another_book.get_info()
        self.assertEqual(rezultat_another, "The Great Gatsby - F. Scott Fitzgerald")
        print('Test 2: Afiseaza informatiile despre alta carte:', rezultat_another)

    def test_is_in_stock_when_stock_is_negative(self):
        # Testează dacă metoda returnează corect False atunci când stocul este negativ.
        book = Book('The Great Gatsby', 'F.Scott Fitzgerald', stock=-3)
        self.assertFalse(book.is_in_stock())
        print('Test 3: Cartea nu ar trebui sa fie in stoc cand stocul este negativ')

    def test_is_in_stock_when_stock_is_positive(self):
        # Testează dacă metoda returnează corect True atunci când stocul este pozitiv.
        book = Book('The Great Gatsby', 'F.Scott Fitzgerald', stock=5)
        self.assertTrue(book.is_in_stock())
        print('Test 4: Cartea ar trebui sa fie in stoc cand stocul este pozitiv')

    def test_is_in_stock_when_stock_is_zero(self):
        # Testează dacă metoda returnează corect False atunci când stocul este zero.
        book = Book('The Great Gatsby', 'F.Scott Fitzgerald', stock=0)
        self.assertFalse(book.is_in_stock())
        print('Test 5: Cartea nu ar trebui sa fie in stoc cand stocul este zero')


    #@unittest.skip
    def test_update_stock(self):
        # Testează actualizarea corectă a stocului cărții.
        book = Book("Dune", "Frank Herbert", stock=4)

        # Adaugă 4 exemplare la stoc.
        book.update_stock(4)
        self.assertEqual(book.stock, 8, "Actualizare incorectă a stocului după adăugarea a 4 exemplare.")
        print('Test 6: Adaugă 4 exemplare la stoc și verifică noul stoc:', book.stock)

        # Scoate 2 exemplare din stoc.
        book.update_stock(-2)
        self.assertEqual(book.stock, 6, "Actualizare incorectă a stocului după scoaterea a 2 exemplare.")
        print('Test 7: Scoate 2 exemplare din stoc și verifică noul stoc:', book.stock)

        # Asigură-te că stocul nu devine negativ.
        book.update_stock(-6)
        self.assertEqual(book.stock, 0, "Stocul ar trebui să fie 0 după ce s-au scos 6 exemplare.")
        print('Test 8: Asigură-te că stocul nu devine negativ și verifică noul stoc:', book.stock)

    def test_update_stock_negative(self):
        # Testează actualizarea stocului cu o valoare negativă.
        book = Book("1984", "George Orwell", stock=5)
        book.update_stock(-3)
        self.assertEqual(book.stock, 2)
        print('Test 9: Verifică actualizarea stocului cu o valoare negativă:', book.stock)

    def test_book_str_representation(self):
        # Testează reprezentarea sub formă de string a cartii.
        book = Book("1984", "George Orwell", stock=5)
        expected_str = "1984 - George Orwell (Stock: 5)"
        self.assertEqual(str(book), expected_str)
        print('Test: Verifică reprezentarea sub formă de string a cartii:', str(book))

    def test_update_stock_zero(self):
        # Testează actualizarea stocului cu valoarea zero.
        book = Book("1984", "George Orwell", stock=5)
        book.update_stock(0)
        self.assertEqual(book.stock, 5)
        print('Test 10: Verifică actualizarea stocului cu valoarea zero:', book.stock)

    def test_update_stock_multiple_times(self):
        # Testează actualizarea stocului de mai multe ori consecutiv.
        book = Book("1984", "George Orwell", stock=0)
        book.update_stock(3)
        book.update_stock(2)
        self.assertEqual(book.stock, 5)
        print('Test: Verifică actualizarea stocului de mai multe ori consecutiv:', book.stock)

    #@unittest.expectedFailure
    def test_update_stock_large_quantity(self):
        # Testează actualizarea stocului cu o valoare mare.
        book = Book("1984", "George Orwell", stock=5)
        book.update_stock(1000)
        self.assertEqual(book.stock, 1005)
        print('Test: Verifică actualizarea stocului cu o valoare mare:', book.stock)


























































