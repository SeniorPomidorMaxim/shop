from django import forms
from .models import *

class AddBookForm(forms.ModelForm):
    class Mets:
        models = Book
        fields = ['title','authors','release_date','genres']