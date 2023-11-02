from typing import Any
from django.shortcuts import render
from .forms import AddBookForm
from .models import Book
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class Home(ListView):
    model = Book
    template_name = 'first/home.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
    
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'first/register.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

def login (request):
    return render(request, "first/login.html")

def about_book (request):
    return render(request, "first/about_book.html")

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddBookForm()
    return render(request,'first/add_book.html', context={'form':form})



