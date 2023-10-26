from django.shortcuts import render
from .forms import UsersForm

def login(request):
     form = UsersForm(request.POST or None)

     if request.method == 'POST' and form.is_valid():
          data = form.cleaned_data
          print(data["name"])
          print(data["password"])
          print(data["email"])
          form = form.save()


     return render(request,'authorization/login.html', context= {'form':form})
