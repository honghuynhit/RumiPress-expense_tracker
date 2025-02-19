from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Book, Author, Category
from .forms import BookForm, AuthorForm, CategoryForm
from .models import Category, Book

def report_view(request):
    # Aggregate distribution expenses by category
    category_expenses = (
        Book.objects.values("category__name")
        .annotate(total_expense=Sum("distribution_expense"))
        .order_by("-total_expense")  # Sort by highest expense
    )

    # Prepare data for Chart.js
    labels = [item["category__name"] for item in category_expenses]
    data = [float(item["total_expense"]) for item in category_expenses]

    context = {
        "labels": labels,
        "data": data,
    }
    return render(request, "expense_tracker/report.html", context)

# Manage Books

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "expense_tracker/book_list.html", {"page_obj": page_obj})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "expense_tracker/book_form.html", {"form": form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "expense_tracker/book_form.html", {"form": form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "expense_tracker/book_confirm_delete.html", {"book": book})

# Author Views
def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expense_tracker/author_list.html', {'page_obj': page_obj})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
        print("form: ", form)
    return render(request, 'expense_tracker/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'expense_tracker/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'expense_tracker/author_confirm_delete.html', {'author': author})

# Category Views
def category_list(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'expense_tracker/category_list.html', {'page_obj': page_obj})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'expense_tracker/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'expense_tracker/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'expense_tracker/category_confirm_delete.html', {'category': category})