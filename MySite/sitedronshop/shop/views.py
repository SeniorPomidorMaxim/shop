from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .models import Product
import os

def main(request):
    products = Product.objects.all()
    return render(request, "shop/main.html", {"products": products})


def list_files(request):
    files = os.listdir(settings.MEDIA_ROOT)
    return HttpResponse(files)# костыль для фотографий, потом разобраться

def base(request):
     return render(request,"base.html")

def about(request):
     return render(request,"shop/about.html")

def categories(request):
     category_param = request.GET.get('category_request')
     match category_param:
          case "battery":
               context = {"category": "Аккумуляторы"}
          case "drones":
               context = {"category": "Готовые дроны"}
          case "flight_controllers":
               context = {"category": "Полетные контроллеры"}
          case "speed_regulators":
               context = {"category": "Регуляторы оборотов"}
          case "video_communication_all":
               context = {"category": "ВИДЕОСВЯЗЬ"}
     return render(request, 'shop/categories.html', context)


def categories_list(request):
     category_param = request.GET.get('category_request')
     if category_param is None:
          return HttpResponse('No category parameter supplied', status=400)
     
     categories = {
          'video_communication_all': 'Видеосвязь',
          'motors_all': 'Моторы',
          'frames_all': 'Рамы',
          'radio_communication_all': 'Радиосвязь',
          'screws_all': 'Винты',

     }
     subcategories = {
          'video_communication_all' : ['Аналоговая','Цифровая'],
          'motors_all': ["2207",'2806','2812'],
          'frames_all': ['5', '6', '7', '9'],
          'radio_communication_all': ['Приемники', 'Передатчики'],
          'screws_all': ['5', '6', '7', '9'],
     }
     if category_param not in categories.keys():
          return HttpResponse('Invalid category parameter supplied', status=400)

     context={'selected_category':categories[f'{category_param}'],
          'subcategories' : subcategories[f'{category_param}']
               }
     return render(request, 'shop/categories_list.html', context = context )


# добавлление товара в избранное ## позже доделать
def add_to_favourites(request, product_id):
    # Берем список избранных товаров из сессии или создаем новый, если он не существует
    favourites = request.session.get('favourites', [])

    # Добавляем ID товара в избранное и сохраняем обратно в сессию
    favourites.append(product_id)
    request.session['favourites'] = favourites

    # Возвращаем ответ в виде JSON
    return JsonResponse({'status': 'ok'})
#добавление товара в избранное