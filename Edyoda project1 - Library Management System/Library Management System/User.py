# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    members = []

    @classmethod
    def addMembers(cls, member):
        cls.members.append(member)

    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issuedbook_list = []
        Member.addMembers(self)
        print("Hi {} , welcome to E - Library".format(name))

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    def searchByName(self, name):
        Catalog.searchByName(name)

    def searchByAuthor(self, author):
        Catalog.searchByAuthor(author)

    def displayAllBooks(self):
        Catalog.displayAllBooks()
    # assume name is unique
    def issueBook(self, name, isbn):
        self.issuedbook_list.append(isbn)
        Catalog.removeBookItem(isbn)
        print("Book Issued For 10 Days", name)
        print("Removed Book Name & isbn:", name ,isbn)

    # assume name is unique
    def returnBook(self, name, isbn, rack):
        for book in self.issuedbook_list:
            if isbn not in self.issuedbook_list:
                print("you are returning a wrong book")
            else:
                self.issuedbook_list.remove(isbn)
                Catalog.addBookItem(name, isbn, rack)
                days = int(input("How many days has it been since you issued this book? Be honest! :"))
                d = 10
                if days > d:
                    print("You Have to pay fine of Rs.2/day for late submission" , name)
                    Catalog.addFine(days)
                else:
                    print("Thank You book returned successfully " ,name)
                    print("Returned Book Name & isbn:", name, isbn)


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        Catalog.addBook(name, author, publish_date, pages)

    def addBookItem(self, name, isbn, rack):
        Catalog.addBookItem(name,isbn, rack)

    def removeBook(self,rem_name):
        Catalog.removeBook(rem_name)

    def removeBookItemFromCatalog(self, rem_isbn):
        Catalog.removeBookItem(rem_isbn)

    def displayAllBooks(self):
        Catalog.displayAllBooks()

    def displayMembers(self):
        for member in Member.members:
            print("Name : {} , Member id : {}".format(member.name,member.student_id))

