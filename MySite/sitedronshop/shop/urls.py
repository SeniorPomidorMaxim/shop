from django.urls import path
from .views import add_to_favourites, main,base,categories,categories_list,list_files,about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name = 'main'),
    path('base', base),
    path('categories', categories, name='categories'),
    path('categories_list', categories_list, name='categories_list'),
    path('list_files', list_files, name='list_files'),
    path('about',about, name='about'),
    path('add_to_favourites/<int:product_id>/', add_to_favourites, name = 'add_to_favourites'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)