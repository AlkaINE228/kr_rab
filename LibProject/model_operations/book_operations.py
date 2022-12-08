from models.db_models import *
from fpdf import FPDF
import os

class Lib:
    
    def add_book(title, year, author):
        row = BookModel(
                title=title,
                year=int(year),
                author=author
            )
        row.save()

    def delete_book(title):
        book = BookModel.get(BookModel.title == title.strip())
        book.delete_instance()


    def get_book(book):
            return BookModel(
                author=book.author,
                title=book.title,
                year=book.year
            )

    @staticmethod
    def get_books(books):
        book_list = []
        for book in books:
            book_list.append(
                (
                    book.id,
                    BookModel(
                        author=book.author,
                        title=book.title,
                        year=book.year
                    )
                )
            )
        return book_list

    def get_all_books():
        query = BookModel.select()
        return Lib.get_books(query)

    def find_by_author(author):
        query =  BookModel.select().where(BookModel.author == author)
        return Lib.get_books(query)
        
    def find_by_year(year):
        query =  BookModel.select().where(BookModel.year == year)
        return Lib.get_books(query)
        
    def print_all_books():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 14)

        books=Lib.get_all_books()
        line_index = 1
        for string in books:
            string = str(string)
            string=string.replace('(', '')
            string=string.replace(')', '')
            pdf.cell(200, 10, txt=string, ln=line_index, align="L")
            line_index += 1

        pdf.output('output.pdf')
    