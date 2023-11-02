from django.urls import path
from .views import about_book,add_book,login,Home,RegisterUser

urlpatterns = [
     path('about', about_book, name='about_book'),
     path('add_book', add_book, name='add_book'),
     path('login', login, name='login'),
     path('', Home.as_view() , name='home'),
     path("register", RegisterUser.as_view(), name = 'register')
]