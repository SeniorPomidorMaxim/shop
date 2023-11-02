from django.contrib import admin
from .models import Book,Author,Genre

class  BookAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['id',]



class  AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','id']
    list_filter = ['first_name','last_name','id']



class  GenreAdmin(admin.ModelAdmin):
    list_display = ['name','description','id']
    list_filter = ['name','description','id']

admin.site.register(Genre,GenreAdmin) 

admin.site.register(Book,BookAdmin) 

admin.site.register(Author,AuthorAdmin) 
