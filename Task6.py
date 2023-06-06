#!/usr/bin/python
from xml.etree.ElementTree import parse, Element, SubElement

def ReadBooks():
    file = r"d:\pobrane\Narzędzia Pracy w Branży IT\Lab678\pathFile3.xml"
    books = list()
    doc = parse(file)
    root = doc.getroot()
    for bookElement in root.iterfind("book"):
        title = bookElement.findtext("title")
        book = Book(title)
        book.author = bookElement.findtext("author")
        book.publisher = bookElement.findtext("publisher")
        book.publicationDate = bookElement.findtext("publication_date")
        for chapterElement in bookElement.iterfind("chapters/chapter"):
            title = chapterElement.findtext("title")
            page = chapterElement.findtext("page")
            chapter = Chapter(book, title, page)
            chapter.number = chapterElement.get("number")
            book.chapters.append(chapter)
        book.chapters.sort(key = lambda c : int(c.page))
        books.append(book)
    return books
