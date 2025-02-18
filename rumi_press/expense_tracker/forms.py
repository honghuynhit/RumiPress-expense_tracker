from django import forms
from .models import Book, Author, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
