import peewee
from models.db_models import *
from model_operations.book_operations import *
   
if __name__ == '__main__':
    try:
        print('Введите команду: ')
        command = input("Для добавления книги введите 1\nдля удаления введите 2\nдля поиска по автору введите 3\nдля поиска по году выпуска введите 4\nдля вывода всех книг введите 5\nдля печати всех книг введите 6: ")
        if int(command) == 1:
            title = input('Введите название книги: ')
            year = int(input('Введите год выпуска книги: '))
            author = input('Введите автора книги: ')
            Lib.add_book(title, year, author)
        elif int(command) == 2:
            title = input('Введите название книги для удаления: ')
            Lib.delete_book(title)
        elif int(command) == 3:
            author = input('Введите автора книги: ')
            print(Lib.find_by_author(author))
        elif int(command) == 4:
            year = input('Введите год выпуска книги: ')
            print(Lib.find_by_year(year))
        elif int(command) == 5:
            print(Lib.get_all_books())
        elif int(command) == 6:
            Lib.print_all_books()
        else:
            quit()
    except peewee.InternalError as px:
        print(str(px))