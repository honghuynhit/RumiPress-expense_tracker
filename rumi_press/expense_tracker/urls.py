from django.urls import path
from .views import report_view
from .views import (
    book_list, book_create, book_update, book_delete,
    author_list, author_create, author_update, author_delete,
    category_list, category_create, category_update, category_delete
)

urlpatterns = [
    path("", report_view, name="dashboard"),
    path("report/", report_view, name="report"),
    path("books/", book_list, name="book_list"),
    path("books/new/", book_create, name="book_create"),
    path("books/edit/<str:pk>/", book_update, name="book_update"),
    path("books/delete/<str:pk>/", book_delete, name="book_delete"),
    
    path("authors/", author_list, name="author_list"),
    path("authors/new/", author_create, name="author_create"),
    path("authors/edit/<int:pk>/", author_update, name="author_update"),
    path("authors/delete/<int:pk>/", author_delete, name="author_delete"),
    
    path("categories/", category_list, name="category_list"),
    path("categories/new/", category_create, name="category_create"),
    path("categories/edit/<int:pk>/", category_update, name="category_update"),
    path("categories/delete/<int:pk>/", category_delete, name="category_delete"),
]