# -*- coding: utf-8 -*-
from Book import Book


# First Book is file & second is Class

class Catalog:
    different_book_count = 0
    books = []
    fine = 0

    @classmethod
    # Only available to admin
    def addBooksList(cls, book):
        cls.books.append(book)

    def addFine(days):
        Catalog.fine = (days - 10) * 2
        print("Fine For Late Submission Rs:",Catalog.fine)

    def addBook(name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        Catalog.different_book_count += 1
        Catalog.books.append(b)
        print("Book Added Successfully".format(name))

    def addBookItem(name, isbn, rack):
        for book in Catalog.books:
            if book.name == name:
                b = Book.addBookItem(book, isbn, rack)


    def searchByName(name):
        for book in Catalog.books:
            if book.name == name:
                print("Book Name:", book.name)
                print("Book is Available")
        else:
            print("Book Name:", book.name)
            print("Book is not available",book.name)

    def searchByAuthor(author):
        for book in Catalog.books:
            if book.author == author:
                print("Book Name:",book.name)
                print("Book is Available")
        else:
            print("Book is not available")

    def displayAllBooks():
        print('Different Book Count', Catalog.different_book_count)
        c = 0
        for book in Catalog.books:
            c += book.total_count
            book.printBook()
        print("Total Books" , c)


    def removeBook(rem_name):
        for book in Catalog.books:
            if book.name == rem_name:
                Catalog.books.remove(book)
                Catalog.different_book_count -= 1
                print("Book removed ".format(rem_name))

    def removeBookItem(rem_isbn):
        for book in Catalog.books:
            for book_item in book.book_item:
                if book_item.isbn == rem_isbn:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book Item removed successfully from the catalog")
                    print("Updated Count:",book.total_count)