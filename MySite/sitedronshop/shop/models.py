from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class CategoryAttribute(models.Model):
    category = models.ForeignKey(Category,related_name="attribute", on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.attribute_name}:{self.attribute_value} for {self.category.name}'
    
class Product(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название')
    content = models.TextField(blank=True,verbose_name='Доп информация')
    price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Цена')
    in_stock = models.BooleanField(default=False,verbose_name='В наличие')
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True,verbose_name='Фото')
    weight = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, related_name="products")

    def __str__(self):
        return self.title

