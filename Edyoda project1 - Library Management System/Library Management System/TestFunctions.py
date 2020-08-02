# -*- coding: utf-8 -*-

from User import Member
from User import Librarian

lib = Librarian("Akhila Madhu", "Kerala", 22, "ED65845", "33541567")
print(lib)

lib.addBook('Shoe Dog','Phil Knight', "2015", 312)
lib.addBookItem("Shoe Dog", "123pk", "H1B1")
lib.addBook('Iron Man','Tony Stark', "2001", 800)
lib.addBookItem("Iron Man", "123im", "I1B1")
lib.addBook('Moonwalking with Einstien','J Foer', "2017", 318)
lib.addBookItem("Moonwalking with Einstien", "325ad", "A1B1")
lib.addBookItem("Moonwalking with Einstien", "326ad", "A1B2")
lib.addBook('Harry Potter','J K Rowling', "1997", "312")
lib.addBookItem("Harry Potter", "854hm", "C1B1")

lib.displayAllBooks()
lib.removeBookItemFromCatalog("325ad")
lib.displayAllBooks()
lib.removeBook("Moonwalking with Einstien")
lib.displayAllBooks()

member1 = Member("Ron", "Pune", 21, "LID547895", "STU343231")



member2 = Member("Rhea", "Kerala", 20, "LID43218", "STU656461")


member2.searchByName("Shoe Dog")
member1.searchByAuthor("Steve")
member1.searchByAuthor("Tony Stark")

member1.issueBook("Shoe Dog","123pk")
lib.displayAllBooks()

member1.returnBook("Shoe Dog","123pk","H1B1")
lib.displayAllBooks()
lib.displayMembers()
