from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField('Название', max_length=128)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Имя автора', null=True, max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField('Название издательства', max_length=100)

    '''def __str__(self):
        return self.name'''


class Order(models.Model):
    data = models.DateField()
    books = models.ManyToManyField(Book)

    def __str__(self):
        books = self.books.all()
        books_name = ''
        for book in books:
            books_name += ',' + book.name
        return f'{self.data} {books_name}'


class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, primary_key=True)
