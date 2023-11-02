from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() ## описание
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

     
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
       
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    release_date = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
       
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"