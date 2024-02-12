# Gestionare Carti / Book Management

## Description:

This project is all about making it easy to manage books in a library. It's designed to be simple and friendly for anyone who needs to keep track of books.

## Framework Used:

The project utilizes the built-in Python unit testing framework, unittest. It provides a robust framework for writing and running unit tests in a modular and efficient manner.

## Project Structure:

The project is organized into the following main components:

__book.py__: This is where we describe what a book looks like in our system. We say what information it has and how we can change that info.

__library.py__: Here, we make a blueprint for how our library works. We decide how to add new books, take them away, and look for specific ones. 
                The Library class managing the book collection.

__test_book.py__:  We've written some tests here to check if our book system does what we expect it to. Unit tests for the Book class.

__test_library.py__: Similarly, we've made some tests for our library system to make sure it does its job properly. Unit tests for the Library class.

## Code Structure:

__book.py__

This section contains the definition of the Book class representing a book in the library. The attributes and methods of this class allow manipulation of details about each book.

__library.py__

This section presents the definition of the Library class representing a library and handling the book collection. The methods of the class allow adding, removing, and searching for books in the library.

__test_book.py__

This file contains unit tests to verify the functionalities of the Book class. These tests ensure the correctness of the implementation and the expected behavior of the class.

__test_library.py__

Here, we find unit tests for the Library class. These tests verify the correct functioning of the class methods and the efficient management of books in the library.

## Tests :

Tests have been created to ensure the correctness of key project functionalities. These cover aspects such as adding and removing books, searching, and updating stock.

## How to Run Tests:

Follow these steps to ensure that the project works as intended:

Open the terminal in the project directory.
Run python -m unittest discover -v tests. This will run all the tests and show you if anything's not working as it should.

## Test Report:

After running the tests, here's a summary of what we found:

__Unit Tests__: 10 tests executed with 100% coverage.

__No significant issues were identified during testing.__

Screenshots:

## How to Contribute:

If you want to contribute to the project, follow these steps:

Clone the repository: git clone <repository_URL>.
Create a new branch: git checkout -b branch_name.
Add your changes and commit: git add . and git commit -m "Description of changes".
Send a pull request: git push origin branch_name.

## License:

This project is licensed under the MIT License.

## What's Next:

In the future, new features or improvements may be added. Stay tuned for updates!
