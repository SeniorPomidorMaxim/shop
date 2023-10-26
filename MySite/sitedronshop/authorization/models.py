from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20,verbose_name='Имя пользователя')
    password = models.CharField(max_length=20,verbose_name='Пароль пользователя')
    email = models.EmailField(blank=True, verbose_name='email пользователя')

