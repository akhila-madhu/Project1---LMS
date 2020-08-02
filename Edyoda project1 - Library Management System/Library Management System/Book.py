# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
        
    def __init__(self, name, author, publication_date, pages):
        self.name = name
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        
    def addBookItem(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count +=1
        print("Upadated Count: ",self.total_count)
        
    def printBook(self):
        print ("{} Written by {}".format(self.name, self.author))
        for book_item in self.book_item:
            print ("Isbn: {}, Rack: {}".format(book_item.isbn, book_item.rack))