from peewee import *
 
dbhandle = MySQLDatabase('library', user='admin', password='admin',
                         host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = dbhandle

class BookModel(BaseModel):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100)
    year = IntegerField()
    author = CharField(max_length=100)

    def __str__(self):
        return f'{self.title}, {self.year}, {self.author}'

    def __repr__(self):
        return f'{self.title}, {self.year}, {self.author}'

    class Meta:
        db_table = "books"
        order_by = ("id",)
