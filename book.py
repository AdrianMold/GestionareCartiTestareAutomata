# book.py

# Clasa care reprezintă o carte într-o bibliotecă.
import unittest


class Book(unittest.TestCase):
    def __init__(self, title, author, stock=0):
        # Initializează atributele obiectului: titlu și autor.
        self.title = title
        self.author = author
        self.stock = stock

    def __str__(self):
        return f"{self.title} - {self.author} (Stock: {self.stock})"

    # def get_display_info(self):
    #     return f"{self.title} - {self.author} (Stock: {self.stock})"

    def get_info(self):
        # Returnează informații despre carte.
        return f"{self.title} - {self.author}"

    def update_stock(self, quantity):
        # Actualizează stocul cărții.
        self.stock += quantity
        #print(f'Stocul cartii {self.title} a fost actualizat: {self.author} exemplare disponibile.')

    def is_in_stock(self):
        # Verifica daca cartea este in stoc
        return self.stock > 0





